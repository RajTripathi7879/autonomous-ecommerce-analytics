# E-Commerce Analytics Instructions

## 1. Purpose

Analyze the Superstore e-commerce dataset to identify important
sales, profit, regional, category, discount, and product-level
business trends.

The analysis should support business-oriented decision-making.

---

## 2. Data Source

Primary dataset:

- data/raw/superstore.csv

Processed dataset:

- data/processed/superstore_clean.csv

Database:

- database/superstore.db

Main database table:

- superstore_clean

---

## 3. Required Business Analysis

The analytics pipeline should calculate the following:

### 3.1 Overall Business Performance

Calculate:

- Total Sales
- Total Profit
- Profit Margin Percentage

### 3.2 Sales and Profit by Year

Calculate:

- Total Sales by Year
- Total Profit by Year

Identify significant changes in sales or profit over time.

### 3.3 Sales by Region

Calculate:

- Total Sales by Region

Identify regions with relatively high or low sales.

### 3.4 Profit by Category

Calculate:

- Total Profit by Category

Identify categories contributing significantly to total profit
or generating relatively low profit.

### 3.5 Profit Margin by Region

Calculate:

- Total Sales by Region
- Total Profit by Region
- Profit Margin Percentage by Region

Compare regional profitability.

### 3.6 Discount and Profit Analysis

Analyze:

- Discount Level
- Average Profit
- Total Profit

Identify patterns between discount levels and profitability.

Do not assume that discount alone causes changes in profit.
Describe the relationship as an observed association.

### 3.7 Loss-Making Products

Identify products where:

- Total Profit < 0

Rank loss-making products by total negative profit.

### 3.8 Profit by Sub-Category

Calculate:

- Total Sales by Sub-Category
- Total Profit by Sub-Category

Identify strong and weak sub-categories.

---

## 4. Data Quality Requirements

Before generating business insights:

1. Confirm that the database exists.
2. Confirm that the required table exists.
3. Confirm that the table contains rows.
4. Confirm that required analytical columns exist.
5. Validate that calculated results can be generated successfully.

If validation fails, do not generate business conclusions from
the invalid results.

---

## 5. Analytical Principles

Follow these principles:

- Use calculated data as the source of truth.
- Do not invent numerical values.
- Do not modify calculated results during interpretation.
- Preserve the distinction between sales and profit.
- Preserve the distinction between correlation/association and causation.
- Clearly identify negative-profit products.
- Use precise values internally and rounded values only for presentation.
- Do not claim a metric that is not available in the dataset.

---

## 6. Output Requirements

The analytics pipeline should produce:

1. Raw SQL analysis results
2. Structured business metrics
3. Validation status
4. Business insights
5. Business recommendations

Current structured metrics output:

- outputs/metrics.json

Current raw analysis output:

- outputs/business_analysis.json

---

## 7. Insight Generation

Business insights should be based only on calculated metrics.

Each insight should identify:

- What happened
- Where or when it happened
- The relevant metric
- Why the result may be important for the business

When the available data does not establish a reason,
do not present a possible explanation as a confirmed fact.

---

## 8. Recommendations

Recommendations should be connected to observed business results.

Examples include:

- Reviewing discount strategies
- Investigating significant loss-making products
- Investigating lower-performing regions
- Supporting strong-performing categories or sub-categories
- Investigating factors associated with changes in sales and profit

Recommendations must not claim that an action will definitely
produce a specific business outcome unless the available data
supports that conclusion.

---

## 9. Change Detection

The pipeline should detect whether the source dataset has changed.

If the dataset changes:

- Reprocess the data.
- Recalculate the analytical results.
- Rebuild the structured metrics.
- Regenerate downstream outputs.

Dataset changes should be detected using the dataset contents,
not only the file modification timestamp.

---

## 10. AI Responsibilities

The AI layer may:

- Interpret calculated metrics.
- Identify notable trends.
- Identify potential business questions.
- Generate business-oriented explanations.
- Generate recommendations based on calculated evidence.
- Generate natural-language reports.

The AI layer must NOT:

- Invent metrics.
- Replace Python/SQL calculations.
- Alter calculated values.
- Treat assumptions as facts.
- Claim causation when the data only shows association.
- Generate insights unsupported by the calculated data.

Python and SQL remain the source of truth for numerical analysis.