import json
from pathlib import Path


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

    analysis_results = {
        "analysis_priority": plan["analysis_priority"],
        "business_questions": plan["business_questions"],
        "results": {
            "overall_business_performance": metrics[
                "overall_business_performance"
            ],
            "sales_profit_by_year": metrics[
                "sales_profit_by_year"
            ],
            "sales_by_region": metrics[
                "sales_by_region"
            ],
            "profit_by_category": metrics[
                "profit_by_category"
            ],
            "profit_margin_by_region": metrics[
                "profit_margin_by_region"
            ],
            "discount_profit_analysis": metrics[
                "discount_profit_analysis"
            ],
            "loss_making_products": metrics[
                "loss_making_products"
            ],
            "profit_by_subcategory": metrics[
                "profit_by_subcategory"
            ]
        },
        "validation_checks": plan["insight_checks"]
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(analysis_results, file, indent=4)

    return analysis_results


if __name__ == "__main__":
    print("=" * 60)
    print("AI ANALYSIS EXECUTOR")
    print("=" * 60)

    results = execute_analysis_plan()

    print("\nAnalysis plan executed successfully.")

    print("\nEvidence sections collected:")

    for section in results["results"]:
        print(f"  - {section}")

    print("\nResults saved to:")
    print("outputs/analysis_results.json")