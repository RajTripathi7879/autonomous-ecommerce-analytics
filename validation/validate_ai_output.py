import json
from pathlib import Path


def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def validate_ai_output():
    project_root = Path(__file__).resolve().parent.parent

    report_file = project_root / "outputs" / "final_report.json"
    metrics_file = project_root / "outputs" / "metrics.json"
    results_file = project_root / "outputs" / "analysis_results.json"

    print("\n" + "=" * 60)
    print("AI OUTPUT VALIDATION")
    print("=" * 60)

    if not report_file.exists():
        print("❌ Final AI report not found.")
        return False

    if not metrics_file.exists():
        print("❌ Metrics file not found.")
        return False

    if not results_file.exists():
        print("❌ Analysis results file not found.")
        return False

    report = load_json(report_file)
    metrics = load_json(metrics_file)
    analysis_results = load_json(results_file)

    required_sections = [
        "executive_summary",
        "key_insights",
        "recommendations",
        "source_metrics"
    ]

    missing_sections = [
        section
        for section in required_sections
        if section not in report
    ]

    if missing_sections:
        print(f"❌ Missing report sections: {missing_sections}")
        return False

    print("✓ Required report sections exist")

    if not isinstance(report["key_insights"], list):
        print("❌ key_insights must be a list.")
        return False

    if not isinstance(report["recommendations"], list):
        print("❌ recommendations must be a list.")
        return False

    print("✓ Report structure is valid")

    source_metrics = metrics["overall_business_performance"]
    report_metrics = report["source_metrics"]

    required_metrics = [
        "total_sales",
        "total_profit",
        "profit_margin_percent"
    ]

    for metric in required_metrics:
        if metric not in report_metrics:
            print(f"❌ Missing source metric: {metric}")
            return False

        source_value = float(source_metrics[metric])
        report_value = float(report_metrics[metric])

        if abs(source_value - report_value) > 0.01:
            print(
                f"❌ Metric mismatch: {metric} "
                f"(source={source_value}, report={report_value})"
            )
            return False

    print("✓ Source metrics match Python/SQL results")

    valid_evidence_sources = set(
        analysis_results["results"].keys()
    )

    for index, recommendation in enumerate(
        report["recommendations"],
        start=1
    ):
        if not isinstance(recommendation, dict):
            print(
                f"❌ Recommendation {index} must be an object."
            )
            return False

        required_fields = [
            "area",
            "recommendation",
            "reason",
            "evidence_source"
        ]

        missing_fields = [
            field
            for field in required_fields
            if field not in recommendation
        ]

        if missing_fields:
            print(
                f"❌ Recommendation {index} is missing: "
                f"{missing_fields}"
            )
            return False

        evidence_source = recommendation["evidence_source"]

        if isinstance(evidence_source, list):
            evidence_sources = evidence_source
        else:
            evidence_sources = [
                source.strip()
                for source in evidence_source.split(" and ")
            ]

        invalid_sources = [
            source
            for source in evidence_sources
            if source not in valid_evidence_sources
        ]

        if invalid_sources:
            print(
                f"❌ Recommendation {index} uses invalid "
                f"evidence source(s): {invalid_sources}"
            )
            return False

    print("✓ All recommendations reference valid evidence")

    print("=" * 60)
    print("AI OUTPUT VALIDATION PASSED")
    print("=" * 60)

    return True


if __name__ == "__main__":
    validation_passed = validate_ai_output()

    if not validation_passed:
        raise SystemExit(1)