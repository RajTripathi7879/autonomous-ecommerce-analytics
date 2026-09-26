import json
from pathlib import Path


def load_final_report():
    project_root = Path(__file__).resolve().parent.parent
    report_file = project_root / "outputs" / "final_report.json"

    if not report_file.exists():
        raise FileNotFoundError(
            f"Final report not found: {report_file}"
        )

    with open(report_file, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_markdown_report():
    project_root = Path(__file__).resolve().parent.parent

    output_dir = project_root / "outputs"
    output_file = output_dir / "final_report.md"

    output_dir.mkdir(exist_ok=True)

    report = load_final_report()

    lines = []

    lines.append("# E-Commerce Sales Analytics Report")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(report["executive_summary"])
    lines.append("")

    lines.append("## Key Business Insights")
    lines.append("")

    for insight in report["key_insights"]:
        lines.append(f"### {insight['area']}")
        lines.append("")
        lines.append(f"**Observation:** {insight['observation']}")
        lines.append("")
        lines.append(f"**Evidence:** {insight['evidence']}")
        lines.append("")

    lines.append("## Recommendations")
    lines.append("")

    for recommendation in report["recommendations"]:
        lines.append(f"### {recommendation['area']}")
        lines.append("")
        lines.append(
            f"**Recommendation:** "
            f"{recommendation['recommendation']}"
        )
        lines.append("")
        lines.append(
            f"**Reason:** {recommendation['reason']}"
        )
        lines.append("")
        lines.append(
            f"**Evidence Source:** "
            f"`{recommendation['evidence_source']}`"
        )
        lines.append("")

    lines.append("## Source Metrics")
    lines.append("")

    metrics = report["source_metrics"]

    lines.append("| Metric | Value |")
    lines.append("|---|---:|")
    lines.append(
        f"| Total Sales | ${metrics['total_sales']:,.2f} |"
    )
    lines.append(
        f"| Total Profit | ${metrics['total_profit']:,.2f} |"
    )
    lines.append(
        f"| Profit Margin | "
        f"{metrics['profit_margin_percent']:.2f}% |"
    )
    lines.append("")

    lines.append(
        "> All numerical metrics are sourced from the "
        "Python/SQL analytics layer."
    )
    lines.append("")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return output_file


if __name__ == "__main__":
    print("=" * 60)
    print("REPORT GENERATOR")
    print("=" * 60)

    output_file = generate_markdown_report()

    print("\nHuman-readable report generated successfully.")
    print(f"Report saved to: {output_file}")