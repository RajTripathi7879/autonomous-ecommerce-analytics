import json
from pathlib import Path

import matplotlib.pyplot as plt


def load_metrics():
    project_root = Path(__file__).resolve().parent.parent.parent
    metrics_file = project_root / "outputs" / "metrics.json"

    if not metrics_file.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {metrics_file}"
        )

    with open(metrics_file, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_charts():
    project_root = Path(__file__).resolve().parent.parent.parent
    charts_dir = project_root / "reports" / "charts"

    charts_dir.mkdir(exist_ok=True)

    metrics = load_metrics()

    # 1. Sales and Profit by Year
    yearly_data = metrics["sales_profit_by_year"]

    years = [str(row["year"]) for row in yearly_data]
    sales = [float(row["total_sales"]) for row in yearly_data]
    profits = [float(row["total_profit"]) for row in yearly_data]

    plt.figure(figsize=(10, 6))
    plt.plot(years, sales, marker="o", label="Sales")
    plt.plot(years, profits, marker="o", label="Profit")
    plt.title("Sales and Profit by Year")
    plt.xlabel("Year")
    plt.ylabel("Amount")
    plt.legend()
    plt.tight_layout()
    plt.savefig(
        charts_dir / "sales_profit_by_year.png",
        dpi=150
    )
    plt.close()

    # 2. Sales by Region
    region_data = metrics["sales_by_region"]

    regions = [row["region"] for row in region_data]
    region_sales = [
        float(row["total_sales"])
        for row in region_data
    ]

    plt.figure(figsize=(9, 6))
    plt.bar(regions, region_sales)
    plt.title("Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(
        charts_dir / "sales_by_region.png",
        dpi=150
    )
    plt.close()

    # 3. Profit by Category
    category_data = metrics["profit_by_category"]

    categories = [
        row["category"]
        for row in category_data
    ]

    category_profit = [
        float(row["total_profit"])
        for row in category_data
    ]

    plt.figure(figsize=(9, 6))
    plt.bar(categories, category_profit)
    plt.title("Profit by Category")
    plt.xlabel("Category")
    plt.ylabel("Profit")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(
        charts_dir / "profit_by_category.png",
        dpi=150
    )
    plt.close()

    # 4. Profit Margin by Region
    margin_data = metrics["profit_margin_by_region"]

    margin_regions = [
        row["region"]
        for row in margin_data
    ]

    margins = [
        float(row["profit_margin_percent"])
        for row in margin_data
    ]

    plt.figure(figsize=(9, 6))
    plt.bar(margin_regions, margins)
    plt.title("Profit Margin by Region")
    plt.xlabel("Region")
    plt.ylabel("Profit Margin (%)")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(
        charts_dir / "profit_margin_by_region.png",
        dpi=150
    )
    plt.close()

    # 5. Profit by Sub-Category
    subcategory_data = metrics["profit_by_subcategory"]

    subcategories = [
        row["sub_category"]
        for row in subcategory_data
    ]

    subcategory_profit = [
        float(row["total_profit"])
        for row in subcategory_data
    ]

    plt.figure(figsize=(11, 7))
    plt.barh(subcategories, subcategory_profit)
    plt.title("Profit by Sub-Category")
    plt.xlabel("Profit")
    plt.ylabel("Sub-Category")
    plt.tight_layout()
    plt.savefig(
        charts_dir / "profit_by_subcategory.png",
        dpi=150
    )
    plt.close()

    print("\nCharts generated successfully.")

    print("\nGenerated charts:")
    for chart in sorted(charts_dir.glob("*.png")):
        print(f"  ✓ {chart.name}")


if __name__ == "__main__":
    generate_charts()