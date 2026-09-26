import json
from pathlib import Path


def load_analysis_results():
    project_root = Path(__file__).resolve().parent.parent
    analysis_file = project_root / "outputs" / "analysis_results.json"

    if not analysis_file.exists():
        raise FileNotFoundError(
            f"Analysis results not found: {analysis_file}"
        )

    with open(analysis_file, "r", encoding="utf-8") as file:
        return json.load(file)


def load_anomalies():
    project_root = Path(__file__).resolve().parent.parent
    anomalies_file = project_root / "outputs" / "anomalies.json"

    if not anomalies_file.exists():
        raise FileNotFoundError(
            f"Anomaly results not found: {anomalies_file}"
        )

    with open(anomalies_file, "r", encoding="utf-8") as file:
        return json.load(file)


def build_recommendation_inputs():
    analysis_results = load_analysis_results()
    anomalies = load_anomalies()

    return {
        "analysis_results": analysis_results,
        "anomalies": anomalies,
    }

def generate_rule_based_recommendations(inputs):
    analysis_results = inputs["analysis_results"]
    anomalies = inputs["anomalies"]

    recommendations = []

    anomaly_signals = anomalies.get("anomalies", [])
    selected_tasks = analysis_results.get("selected_tasks", [])

    anomaly_types = {
        anomaly.get("type")
        for anomaly in anomaly_signals
    }

    if "loss_making_products" in selected_tasks:
        recommendations.append({
            "area": "Product Profitability",
            "priority": "High",
            "action": "Review loss-making products and evaluate pricing, discounting, and product-level costs.",
            "evidence": "Loss-making product analysis",
            "trigger": "Products with negative total profit",
        })

    if "negative_discount_profit" in anomaly_types:
        recommendations.append({
            "area": "Discount Strategy",
            "priority": "High",
            "action": "Review discount levels associated with negative total profit and assess whether discounting should be reduced or better targeted.",
            "evidence": "Discount profitability analysis",
            "trigger": "Discount levels with negative total profit",
        })

    if "low_regional_margin" in anomaly_types:
        recommendations.append({
            "area": "Regional Profitability",
            "priority": "Medium",
            "action": "Investigate lower-margin regions by reviewing regional product mix, discounting, and profitability drivers.",
            "evidence": "Regional profit margin analysis",
            "trigger": "Region with materially below-average profit margin",
        })

    if "yearly_profit_change" in anomaly_types:
        recommendations.append({
            "area": "Profit Trend",
            "priority": "Medium",
            "action": "Investigate major year-over-year profit changes to identify the underlying business drivers.",
            "evidence": "Yearly sales and profit analysis",
            "trigger": "Large year-over-year profit change",
        })

    if "yearly_sales_change" in anomaly_types:
        recommendations.append({
            "area": "Sales Trend",
            "priority": "Medium",
            "action": "Investigate major year-over-year sales changes and identify the products, regions, or categories contributing to the change.",
            "evidence": "Yearly sales and profit analysis",
            "trigger": "Large year-over-year sales change",
        })

    return recommendations

def save_recommendations(recommendations):
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "recommendations.json"

    output_dir.mkdir(exist_ok=True)

    result = {
        "recommendation_count": len(recommendations),
        "recommendations": recommendations,
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    return result

if __name__ == "__main__":
    print("=" * 60)
    print("RECOMMENDATION ENGINE")
    print("=" * 60)

    inputs = build_recommendation_inputs()
    recommendations = generate_rule_based_recommendations(inputs)
    result = save_recommendations(recommendations)

    print(
        f"\nGenerated {result['recommendation_count']} recommendations."
    )

    for recommendation in result["recommendations"]:
        print(
            f"  - [{recommendation['priority'].upper()}] "
            f"{recommendation['area']}"
        )

    print("\nResults saved to:")
    print("outputs/recommendations.json")