import json
from pathlib import Path


TASK_TO_METRIC = {
    "overall_business_performance": "overall_business_performance",
    "sales_profit_by_year": "sales_profit_by_year",
    "regional_performance": [
        "sales_by_region",
        "profit_margin_by_region",
    ],
    "category_profitability": [
        "profit_by_category",
        "profit_by_subcategory",
    ],
    "discount_profitability": "discount_profit_analysis",
    "loss_making_products": "loss_making_products",
}


def load_execution_inputs():
    project_root = Path(__file__).resolve().parent.parent

    plan_file = project_root / "outputs" / "analysis_plan.json"
    metrics_file = project_root / "outputs" / "metrics.json"

    if not plan_file.exists():
        raise FileNotFoundError(
            f"Analysis plan not found: {plan_file}"
        )

    if not metrics_file.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {metrics_file}"
        )

    with open(plan_file, "r", encoding="utf-8") as file:
        plan = json.load(file)

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    return plan, metrics


def execute_analysis_plan():
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "analysis_results.json"

    output_dir.mkdir(exist_ok=True)

    plan, metrics = load_execution_inputs()

    selected_tasks = plan.get("analysis_tasks", [])

    if not selected_tasks:
        raise ValueError(
            "AI planner returned no analysis tasks."
        )

    analysis_results = {}

    for task in selected_tasks:

        if task not in TASK_TO_METRIC:
            raise ValueError(
                f"Unknown analysis task returned by AI planner: {task}"
            )

        metric_sources = TASK_TO_METRIC[task]

        if isinstance(metric_sources, str):
            metric_sources = [metric_sources]

        for metric_name in metric_sources:

            if metric_name not in metrics:
                raise KeyError(
                    f"Required metric '{metric_name}' "
                    f"for task '{task}' was not found."
                )

            analysis_results[metric_name] = metrics[metric_name]

    execution_output = {
        "selected_tasks": selected_tasks,
        "analysis_priority": plan.get(
            "analysis_priority",
            []
        ),
        "business_questions": plan.get(
            "business_questions",
            []
        ),
        "results": analysis_results,
        "validation_checks": plan.get(
            "insight_checks",
            []
        ),
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            execution_output,
            file,
            indent=4
        )

    return execution_output


if __name__ == "__main__":
    print("=" * 60)
    print("AI ANALYSIS EXECUTOR")
    print("=" * 60)

    results = execute_analysis_plan()

    print("\nAnalysis plan executed successfully.")

    print("\nSelected tasks:")

    for task in results["selected_tasks"]:
        print(f"  - {task}")

    print("\nEvidence sections collected:")

    for section in results["results"]:
        print(f"  - {section}")

    print("\nResults saved to:")
    print("outputs/analysis_results.json")