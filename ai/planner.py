import json
from pathlib import Path

from google import genai

from ai.config import GEMINI_API_KEY, GEMINI_MODEL
from analytics.instruction_loader import load_analytics_instructions


VALID_ANALYSIS_TASKS = [
    "overall_business_performance",
    "sales_profit_by_year",
    "regional_performance",
    "category_profitability",
    "discount_profitability",
    "loss_making_products",
]


def load_planner_inputs():
    project_root = Path(__file__).resolve().parent.parent

    metrics_file = project_root / "outputs" / "metrics.json"
    anomalies_file = project_root / "outputs" / "anomalies.json"

    if not metrics_file.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {metrics_file}"
        )

    if not anomalies_file.exists():
        raise FileNotFoundError(
            f"Anomalies file not found: {anomalies_file}"
        )

    instructions = load_analytics_instructions()

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    with open(anomalies_file, "r", encoding="utf-8") as file:
        anomalies = json.load(file)

    return instructions, metrics, anomalies

def create_analysis_plan():
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "analysis_plan.json"

    output_dir.mkdir(exist_ok=True)

    instructions, metrics, anomalies = load_planner_inputs()

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are the planning agent for an autonomous e-commerce analytics system.

Your job is to decide which predefined analytical tasks should be
executed based on the supplied analytics instructions, calculated metrics,
and detected anomaly signals.

IMPORTANT RULES:
- Python and SQL calculated metrics are the source of truth.
- Do not invent numerical values.
- Do not modify or recalculate metrics.
- Do not claim causation when the data only shows association.
- Only select tasks from the VALID ANALYSIS TASKS list.
- Do not create new task names.
- Select only tasks that are relevant to the supplied data and instructions.
- The selected tasks will be executed later by Python analytics components.
- Use detected anomaly signals to prioritize relevant analytical tasks.
- An anomaly signal is evidence that an area may require deeper investigation.
- Do not treat an anomaly signal as proof of causation.
- Do not invent additional anomalies.
- Preserve the distinction between detected signals and business conclusions.
- If an anomaly signal is relevant to a predefined task, select that task.
- Use the exact metric names and concepts present in the supplied evidence.
- Do not convert total profit into profit margin, revenue into sales growth,
  or any other metric into a different metric.
- When describing an anomaly, use the evidence source's actual measure.
- Do not introduce a metric that is not present in the supplied evidence.

VALID ANALYSIS TASKS:

{json.dumps(VALID_ANALYSIS_TASKS, indent=2)}

TASK DEFINITIONS:

- overall_business_performance:
  Evaluate total sales, total profit, and profit margin.

- sales_profit_by_year:
  Analyze yearly sales and profit trends.

- regional_performance:
  Analyze regional sales and regional profit margins.

- category_profitability:
  Analyze category and sub-category profitability.

- discount_profitability:
  Analyze the observed association between discount levels and profitability.

- loss_making_products:
  Identify and rank products with negative total profit.

Return ONLY valid JSON.

Required JSON structure:

{{
    "analysis_tasks": [
        "valid_task_name"
    ],
    "analysis_priority": [
        "..."
    ],
    "business_questions": [
        "..."
    ],
    "insight_checks": [
        "..."
    ],
    "report_sections": [
        "..."
    ]
}}

ANALYTICS INSTRUCTIONS:
{instructions}

CALCULATED METRICS:
{json.dumps(metrics, indent=2)}

DETECTED ANOMALY SIGNALS:
{json.dumps(anomalies, indent=2)}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    plan = json.loads(response.text)

    if "analysis_tasks" not in plan:
        raise ValueError(
            "AI planner did not return analysis_tasks."
        )

    invalid_tasks = [
        task
        for task in plan["analysis_tasks"]
        if task not in VALID_ANALYSIS_TASKS
    ]

    if invalid_tasks:
        raise ValueError(
            f"AI planner returned invalid analysis tasks: {invalid_tasks}"
        )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=4)

    return plan


if __name__ == "__main__":
    print("=" * 60)
    print("AI ANALYSIS PLANNER")
    print("=" * 60)

    plan = create_analysis_plan()

    print("\nAnalysis plan created successfully.")

    print("\nSelected analysis tasks:")

    for task in plan["analysis_tasks"]:
        print(f"  - {task}")

    print("\nPriority areas:")

    for item in plan["analysis_priority"]:
        print(f"  - {item}")

    print("\nBusiness questions:")

    for question in plan["business_questions"]:
        print(f"  - {question}")

    print("\nPlan saved to:")
    print("outputs/analysis_plan.json")