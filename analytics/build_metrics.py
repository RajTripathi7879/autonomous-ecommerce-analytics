import json
from pathlib import Path


def build_metrics():
    # Project directories
    project_root = Path(__file__).resolve().parent.parent

    input_file = project_root / "outputs" / "business_analysis.json"
    output_file = project_root / "outputs" / "metrics.json"

    # Load SQL results
    with open(input_file, "r", encoding="utf-8") as file:
        analysis_results = json.load(file)

    # Extract results by query number
    results = {
        item["query_number"]: item
        for item in analysis_results
    }

    # Query 1: Overall business performance
    overall = results[1]["rows"][0]

    metrics = {
        "overall_business_performance": {
            "total_sales": overall[0],
            "total_profit": overall[1],
            "profit_margin_percent": overall[2]
        },

        # Query 2: Sales and profit by year
        "sales_profit_by_year": [
            {
                "year": row[0],
                "total_sales": row[1],
                "total_profit": row[2]
            }
            for row in results[2]["rows"]
        ],

        # Query 3: Sales by region
        "sales_by_region": [
            {
                "region": row[0],
                "total_sales": row[1]
            }
            for row in results[3]["rows"]
        ],

        # Query 4: Profit by category
        "profit_by_category": [
            {
                "category": row[0],
                "total_profit": row[1]
            }
            for row in results[4]["rows"]
        ],

        # Query 5: Profit margin by region
        "profit_margin_by_region": [
            {
                "region": row[0],
                "total_sales": row[1],
                "total_profit": row[2],
                "profit_margin_percent": row[3]
            }
            for row in results[5]["rows"]
        ],

        # Query 6: Discount vs profit
        "discount_profit_analysis": [
            {
                "discount": row[0],
                "average_profit": row[1],
                "total_profit": row[2]
            }
            for row in results[6]["rows"]
        ],

        # Query 7: Loss-making products
        "loss_making_products": [
            {
                "product_name": row[0],
                "total_profit": row[1]
            }
            for row in results[7]["rows"]
        ],

        # Query 8: Profit by sub-category
        "profit_by_subcategory": [
            {
                "sub_category": row[0],
                "total_sales": row[1],
                "total_profit": row[2]
            }
            for row in results[8]["rows"]
        ]
    }

    # Save structured metrics
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            metrics,
            file,
            indent=4,
            default=str
        )

    print("\nMetrics built successfully.")
    print(f"Metrics saved to: {output_file}")


if __name__ == "__main__":
    build_metrics()