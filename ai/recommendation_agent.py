import json
from pathlib import Path

from google import genai

from ai.config import GEMINI_API_KEY, GEMINI_MODEL


def load_recommendation_inputs():
    project_root = Path(__file__).resolve().parent.parent

    recommendations_file = (
        project_root / "outputs" / "recommendations.json"
    )
    analysis_file = (
        project_root / "outputs" / "analysis_results.json"
    )
    metrics_file = (
        project_root / "outputs" / "metrics.json"
    )

    for file_path in [
        recommendations_file,
        analysis_file,
        metrics_file,
    ]:
        if not file_path.exists():
            raise FileNotFoundError(
                f"Required input not found: {file_path}"
            )

    with open(recommendations_file, "r", encoding="utf-8") as file:
        recommendations = json.load(file)

    with open(analysis_file, "r", encoding="utf-8") as file:
        analysis_results = json.load(file)

    with open(metrics_file, "r", encoding="utf-8") as file:
        metrics = json.load(file)

    return {
        "recommendations": recommendations,
        "analysis_results": analysis_results,
        "metrics": metrics,
    }


def create_ai_recommendations():
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured.")

    inputs = load_recommendation_inputs()

    client = genai.Client(api_key=GEMINI_API_KEY)

    prompt = f"""
You are a business analytics recommendation assistant.

Your job is to refine evidence-based recommendations using only
the supplied analytics evidence.

Do not invent metrics, causes, trends, or business facts.

Preserve the distinction between:
- observed evidence
- possible explanation
- recommended action

If the evidence does not establish a cause, describe it as something
that should be investigated rather than stating it as fact.

Return valid JSON only.

Required JSON structure:
{{
    "recommendations": [
        {{
            "area": "string",
            "priority": "High|Medium|Low",
            "recommendation": "string",
            "reason": "string",
            "evidence_source": "string"
        }}
    ]
}}

Evidence-based recommendations:
{json.dumps(inputs["recommendations"], indent=2)}

Analysis results:
{json.dumps(inputs["analysis_results"], indent=2)}

Metrics:
{json.dumps(inputs["metrics"], indent=2)}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text
def save_ai_recommendations(ai_response):
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "ai_recommendations.json"

    output_dir.mkdir(exist_ok=True)

    cleaned_response = ai_response.strip()

    if cleaned_response.startswith("```json"):
        cleaned_response = cleaned_response[7:]

    if cleaned_response.endswith("```"):
        cleaned_response = cleaned_response[:-3]

    cleaned_response = cleaned_response.strip()

    recommendations = json.loads(cleaned_response)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(recommendations, file, indent=4)

    return output_file


if __name__ == "__main__":
    print("=" * 60)
    print("AI RECOMMENDATION AGENT")
    print("=" * 60)

    response = create_ai_recommendations()
    output_file = save_ai_recommendations(response)

    print("\nAI recommendations generated successfully.")
    print(f"Results saved to: {output_file}")
