import json
from pathlib import Path

from google import genai

from ai.config import GEMINI_API_KEY, GEMINI_MODEL
from analytics.instruction_loader import load_analytics_instructions


def load_planner_inputs():
    project_root = Path(__file__).resolve().parent.parent

    metrics_file = project_root / "outputs" / "metrics.json"

    if not metrics_file.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {metrics_file}"
        )

    instructions = load_analytics_instructions()

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    return instructions, metrics


def create_analysis_plan():
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "analysis_plan.json"

    output_dir.mkdir(exist_ok=True)

    instructions, metrics = load_planner_inputs()

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are the planning agent for an autonomous e-commerce analytics system.

Your job is to create an analytical plan using ONLY the supplied
analytics instructions and calculated metrics.

IMPORTANT RULES:
- Python and SQL calculated metrics are the source of truth.
- Do not invent numerical values.
- Do not modify or recalculate metrics.
- Do not claim causation when the data only shows association.
- Focus on meaningful business analysis.
- Identify the most important areas that should be discussed.
- The plan will be executed later by Python analytics components.

Return ONLY valid JSON.

Required JSON structure:

{{
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
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    plan = json.loads(response.text)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(plan, file, indent=4)

    return plan


if __name__ == "__main__":
    print("=" * 60)
    print("AI ANALYSIS PLANNER")
    print("=" * 60)

    plan = create_analysis_plan()

    print("\nAnalysis plan created successfully.")
    print("\nPriority areas:")

    for item in plan["analysis_priority"]:
        print(f"  - {item}")

    print("\nBusiness questions:")

    for question in plan["business_questions"]:
        print(f"  - {question}")

    print("\nPlan saved to:")
    print("outputs/analysis_plan.json")