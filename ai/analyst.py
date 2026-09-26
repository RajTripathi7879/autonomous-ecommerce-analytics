import json
from pathlib import Path

from google import genai

from ai.config import GEMINI_API_KEY, GEMINI_MODEL
from analytics.instruction_loader import load_analytics_instructions


def load_analysis_inputs():
    project_root = Path(__file__).resolve().parent.parent

    results_file = project_root / "outputs" / "analysis_results.json"

    if not results_file.exists():
        raise FileNotFoundError(
            f"Analysis results not found: {results_file}"
        )

    instructions = load_analytics_instructions()

    with open(results_file, "r", encoding="utf-8") as file:
        analysis_results = json.load(file)

    return instructions, analysis_results


def generate_final_report():
    project_root = Path(__file__).resolve().parent.parent

    output_dir = project_root / "outputs"
    output_file = output_dir / "final_report.json"

    output_dir.mkdir(exist_ok=True)

    instructions, analysis_results = load_analysis_inputs()

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are the reporting analyst for an autonomous e-commerce analytics system.

Create a concise business report from the supplied calculated analysis results.

STRICT RULES:
- Python and SQL results are the only source of numerical truth.
- Never invent, estimate, or change numerical values.
- Do not perform new calculations.
- Do not introduce external facts.
- Do not claim causation when the data only shows an association.
- Every recommendation must be directly supported by the supplied evidence.
- Every recommendation must include a valid evidence_source.
- Keep observations factual and business-focused.

Return ONLY valid JSON using exactly this structure:

{{
    "executive_summary": "...",
    "key_insights": [
        {{
            "area": "...",
            "observation": "...",
            "evidence": "..."
        }}
    ],
    "recommendations": [
        {{
            "area": "...",
            "recommendation": "...",
            "reason": "...",
            "evidence_source": "..."
        }}
    ],
    "source_metrics": {{
        "total_sales": 0,
        "total_profit": 0,
        "profit_margin_percent": 0
    }}
}}

CALCULATED ANALYSIS RESULTS:
{json.dumps(analysis_results, indent=2)}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    report = json.loads(response.text)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return report


if __name__ == "__main__":
    print("=" * 60)
    print("AI BUSINESS ANALYST")
    print("=" * 60)

    report = generate_final_report()

    print("\nFinal business report generated successfully.")

    print("\nKey insights:")
    for insight in report["key_insights"]:
        print(f"  - {insight['area']}: {insight['observation']}")

    print("\nRecommendations:")
    for recommendation in report["recommendations"]:
        print(
            f"  - {recommendation['area']}: "
            f"{recommendation['recommendation']}"
        )

    print("\nReport saved to:")
    print("outputs/final_report.json")