import json
from pathlib import Path


def load_metrics():
    project_root = Path(__file__).resolve().parent.parent
    metrics_file = project_root / "outputs" / "metrics.json"

    if not metrics_file.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {metrics_file}"
        )

    with open(metrics_file, "r", encoding="utf-8") as file:
        return json.load(file)


def detect_anomalies():
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "outputs"
    output_file = output_dir / "anomalies.json"

    output_dir.mkdir(exist_ok=True)

    metrics = load_metrics()

    anomalies = []

    # ---------------------------------------------------------
    # 1. Year-over-year sales and profit changes
    # ---------------------------------------------------------

    yearly_data = metrics.get("sales_profit_by_year", [])

    for index in range(1, len(yearly_data)):
        previous = yearly_data[index - 1]
        current = yearly_data[index]

        previous_sales = previous["total_sales"]
        current_sales = current["total_sales"]

        previous_profit = previous["total_profit"]
        current_profit = current["total_profit"]

        if previous_sales != 0:
            sales_change_percent = (
                (current_sales - previous_sales)
                / abs(previous_sales)
            ) * 100

            if abs(sales_change_percent) >= 20:
                anomalies.append({
                    "type": "yearly_sales_change",
                    "severity": "high",
                    "period": str(current["year"]),
                    "description": (
                        f"Sales changed by "
                        f"{sales_change_percent:.2f}% "
                        f"from {previous['year']} to "
                        f"{current['year']}."
                    ),
                    "evidence_source": "sales_profit_by_year"
                })

        if previous_profit != 0:
            profit_change_percent = (
                (current_profit - previous_profit)
                / abs(previous_profit)
            ) * 100

            if abs(profit_change_percent) >= 20:
                anomalies.append({
                    "type": "yearly_profit_change",
                    "severity": "high",
                    "period": str(current["year"]),
                    "description": (
                        f"Profit changed by "
                        f"{profit_change_percent:.2f}% "
                        f"from {previous['year']} to "
                        f"{current['year']}."
                    ),
                    "evidence_source": "sales_profit_by_year"
                })

    # ---------------------------------------------------------
    # 2. Low regional profit margins
    # ---------------------------------------------------------

    regional_data = metrics.get(
        "profit_margin_by_region",
        []
    )

    if regional_data:
        margins = [
            item["profit_margin_percent"]
            for item in regional_data
        ]

        average_margin = sum(margins) / len(margins)

        for item in regional_data:
            if item["profit_margin_percent"] < average_margin * 0.75:
                anomalies.append({
                    "type": "low_regional_margin",
                    "severity": "medium",
                    "period": item["region"],
                    "description": (
                        f"{item['region']} has a profit margin of "
                        f"{item['profit_margin_percent']:.2f}%, "
                        f"which is materially below the "
                        f"regional average of "
                        f"{average_margin:.2f}%."
                    ),
                    "evidence_source": "profit_margin_by_region"
                })

    # ---------------------------------------------------------
    # 3. Grouped loss-making product signal
    # ---------------------------------------------------------

    loss_products = metrics.get(
        "loss_making_products",
        []
    )

    negative_products = [
        product
        for product in loss_products
        if product["total_profit"] < 0
    ]

    if negative_products:
        top_loss_products = negative_products[:10]

        anomalies.append({
            "type": "loss_making_products",
            "severity": "high",
            "period": "product_portfolio",
            "count": len(negative_products),
            "top_products": [
                {
                    "product_name": product["product_name"],
                    "total_profit": product["total_profit"]
                }
                for product in top_loss_products
            ],
            "description": (
                f"{len(negative_products)} products have negative "
                f"total profit. The anomaly signal includes the "
                f"top {len(top_loss_products)} loss-making products "
                f"for deeper investigation."
            ),
            "evidence_source": "loss_making_products"
        })

    # ---------------------------------------------------------
    # 4. Grouped negative-profit discount signal
    # ---------------------------------------------------------

    discount_data = metrics.get(
        "discount_profit_analysis",
        []
    )

    negative_discount_levels = [
        item
        for item in discount_data
        if item["total_profit"] < 0
    ]

    if negative_discount_levels:
        anomalies.append({
            "type": "negative_discount_profit",
            "severity": "medium",
            "period": "discount_levels",
            "count": len(negative_discount_levels),
            "affected_discount_levels": [
                {
                    "discount": item["discount"],
                    "total_profit": item["total_profit"]
                }
                for item in negative_discount_levels
            ],
            "description": (
                f"{len(negative_discount_levels)} discount levels "
                f"have negative total profit. This indicates an "
                f"area for deeper profitability investigation."
            ),
            "evidence_source": "discount_profit_analysis"
        })

    anomaly_output = {
        "anomaly_count": len(anomalies),
        "anomalies": anomalies
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            anomaly_output,
            file,
            indent=4
        )

    return anomaly_output


if __name__ == "__main__":
    print("=" * 60)
    print("ANOMALY DETECTION")
    print("=" * 60)

    results = detect_anomalies()

    print(
        f"\nDetected {results['anomaly_count']} anomaly signals."
    )

    for anomaly in results["anomalies"]:
        print(
            f"  - [{anomaly['severity'].upper()}] "
            f"{anomaly['type']}: "
            f"{anomaly['period']}"
        )

    print("\nResults saved to:")
    print("outputs/anomalies.json")