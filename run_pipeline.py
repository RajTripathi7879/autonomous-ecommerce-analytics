from pathlib import Path

from database.load_database import load_database
from database.run_analysis import run_analysis
from validation.validate_data import validate_data
from validation.validate_ai_output import validate_ai_output
from analytics.build_metrics import build_metrics
from state.detect_changes import check_for_changes
from analytics.instruction_loader import load_analytics_instructions
from ai.planner import create_analysis_plan
from ai.executor import execute_analysis_plan
from ai.analyst import generate_final_report
from reports.generate_report import generate_markdown_report
from reports.charts.generate_charts import generate_charts


PROJECT_ROOT = Path(__file__).resolve().parent


def outputs_are_complete():
    required_outputs = [
        PROJECT_ROOT / "outputs" / "business_analysis.json",
        PROJECT_ROOT / "outputs" / "metrics.json",
        PROJECT_ROOT / "outputs" / "analysis_plan.json",
        PROJECT_ROOT / "outputs" / "analysis_results.json",
        PROJECT_ROOT / "outputs" / "final_report.json",
        PROJECT_ROOT / "outputs" / "final_report.md",
        PROJECT_ROOT / "reports" / "charts" / "profit_by_category.png",
        PROJECT_ROOT / "reports" / "charts" / "profit_by_subcategory.png",
        PROJECT_ROOT / "reports" / "charts" / "profit_margin_by_region.png",
        PROJECT_ROOT / "reports" / "charts" / "sales_by_region.png",
        PROJECT_ROOT / "reports" / "charts" / "sales_profit_by_year.png",
    ]

    return all(output.exists() for output in required_outputs)


print("=" * 60)
print("E-COMMERCE AUTONOMOUS ANALYTICS PIPELINE")
print("=" * 60)

print("\nStep 1: Loading analytics instructions...")
instructions = load_analytics_instructions()

print(
    f"✓ Analytics instructions loaded "
    f"({len(instructions.splitlines())} lines)."
)

print("\nStep 2: Checking for dataset changes...")
dataset_changed = check_for_changes()

if dataset_changed:
    print("✓ Dataset status: CHANGED")
else:
    print("✓ Dataset status: UNCHANGED")

if not dataset_changed and outputs_are_complete():
    print("\n" + "=" * 60)
    print("NO NEW DATA DETECTED")
    print("=" * 60)
    print("✓ Existing analysis outputs are available.")
    print("✓ Full analytics pipeline skipped.")
    print("✓ Existing results remain unchanged.")
    print("=" * 60)
    raise SystemExit(0)

if not dataset_changed:
    print("\n⚠ Dataset is unchanged, but required outputs are missing.")
    print("Running the pipeline to rebuild the outputs.")

print("\nStep 3: Loading data into database...")
load_database()

print("\nStep 4: Running business analysis...")
run_analysis()

print("\nStep 5: Validating data...")
validation_passed = validate_data()

if not validation_passed:
    print("\n❌ Pipeline stopped because data validation failed.")
    raise SystemExit(1)

print("\nStep 6: Building structured business metrics...")
build_metrics()

print("\nStep 7: Running AI analysis planner...")
analysis_plan = create_analysis_plan()

print(
    f"✓ AI planner created "
    f"{len(analysis_plan['analysis_priority'])} priority areas."
)

print("\nStep 8: Executing AI analysis plan...")
analysis_results = execute_analysis_plan()

print(
    f"✓ Analysis evidence collected "
    f"({len(analysis_results['results'])} sections)."
)

print("\nStep 9: Generating AI business report...")
final_report = generate_final_report()

print(
    f"✓ AI report generated with "
    f"{len(final_report['key_insights'])} key insights and "
    f"{len(final_report['recommendations'])} recommendations."
)

print("\nStep 10: Validating AI output...")
ai_validation_passed = validate_ai_output()

if not ai_validation_passed:
    print("\n❌ Pipeline stopped because AI output validation failed.")
    raise SystemExit(1)

print("\nStep 11: Generating human-readable report...")
report_file = generate_markdown_report()

print(
    f"✓ Human-readable report generated: "
    f"{report_file}"
)    

print("\nStep 12: Generating analytical charts...")
generate_charts()

print("✓ Analytical charts generated successfully.")

print("\n" + "=" * 60)
print("AUTONOMOUS ANALYTICS PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated outputs:")
print("  ✓ outputs/business_analysis.json")
print("  ✓ outputs/metrics.json")
print("  ✓ outputs/analysis_plan.json")
print("  ✓ outputs/analysis_results.json")
print("  ✓ outputs/final_report.json")
print("  ✓ outputs/final_report.md")
print("  ✓ reports/charts/*.png")