# Autonomous E-Commerce Analytics System

An AI-assisted autonomous analytics system that transforms e-commerce transaction data into business insights, recommendations, reports, and visualizations with minimal manual intervention.

The project started as a traditional **Python + SQL + Power BI analytics project** and evolved into an automated, AI-assisted pipeline that can detect dataset changes, rebuild the analytical layer, identify anomalies, generate an analysis plan, execute evidence-based analysis, produce recommendations, validate AI outputs, and refresh reports and charts.

---

## Project Overview

The system analyzes the Superstore e-commerce dataset across:

- Sales and profit trends
- Regional performance
- Category and sub-category profitability
- Discount and profit relationships
- Loss-making products
- Business anomalies and areas requiring attention

The core architecture follows a simple principle:

> **Python and SQL calculate the facts. AI interprets the facts.**

This keeps numerical calculations deterministic while using AI for planning, interpretation, and business-oriented reporting.

---

## What Makes This Project Different

A traditional analytics workflow:

```text
Dataset
   ↓
Python / SQL Analysis
   ↓
Power BI Dashboard
   ↓
Manual Interpretation
```

This project extends it to:

```text
Dataset
   ↓
Change Detection
   ↓
Data Validation
   ↓
SQLite Database
   ↓
SQL Analytics
   ↓
Structured Metrics
   ↓
Anomaly Detection
   ↓
AI Planning
   ↓
Analysis Execution
   ↓
AI Recommendations
   ↓
AI Output Validation
   ↓
Business Report + Charts
   ↓
Power BI
```

The result combines:

- Deterministic analytics
- AI-assisted planning and interpretation
- Anomaly detection
- Evidence-based recommendations
- Validation
- Automation
- Business intelligence

---

## System Architecture

```text
                    ┌─────────────────────┐
                    │  Superstore CSV     │
                    │   Raw E-Commerce    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Change Detection   │
                    │      SHA-256        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Validation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ SQLite + SQL        │
                    │ Business Analysis   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Structured Metrics  │
                    │       JSON          │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │ Anomaly Detection│        │ AI Planning Agent│
       └────────┬─────────┘        │     Gemini       │
                │                  └────────┬─────────┘
                │                           │
                └─────────────┬─────────────┘
                              ▼
                    ┌─────────────────────┐
                    │ Analysis Executor   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Recommendation      │
                    │ Engine + AI Refining │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ AI Output Validation│
                    └──────────┬──────────┘
                               │
                     ┌─────────┴─────────┐
                     ▼                   ▼
             ┌──────────────┐    ┌──────────────┐
             │ Business     │    │ Analytical   │
             │ Report       │    │ Charts       │
             └──────────────┘    └──────────────┘
                     │                   │
                     └─────────┬─────────┘
                               ▼
                        ┌────────────┐
                        │  Power BI  │
                        └────────────┘
```

---

## Autonomous Pipeline

The complete workflow is orchestrated by:

```text
run_pipeline.py
```

When a new version of the dataset is detected, the pipeline can automatically:

1. Load analytical instructions
2. Detect source-data changes
3. Rebuild the SQLite analytical database
4. Validate the database and required fields
5. Execute SQL business analyses
6. Build structured metrics
7. Detect business anomalies
8. Generate an AI analysis plan
9. Execute the selected analytical tasks
10. Generate evidence-based recommendations
11. Refine recommendations using AI
12. Generate the AI business report
13. Validate AI outputs against calculated evidence
14. Generate the final Markdown report
15. Generate analytical charts

If the dataset has not changed, the pipeline skips unnecessary processing and AI API calls.

---

## Core Design Principle

```text
                 SOURCE OF TRUTH
                       │
              ┌────────┴────────┐
              │                 │
             SQL              Python
              │                 │
              └────────┬────────┘
                       │
              Calculated Metrics
                       │
                       ▼
                      AI
                       │
                Interpretation
                       │
                       ▼
                Business Report
```

AI does not independently calculate important business metrics from raw transactional records.

- **SQL** performs deterministic business calculations.
- **Python** processes, validates, orchestrates, and detects changes/anomalies.
- **AI** plans analysis, interprets evidence, and produces business-oriented recommendations.
- **Power BI** provides interactive visualization.

---

## Dataset

The project uses the Superstore e-commerce dataset.

```text
data/raw/superstore.csv
data/processed/superstore_clean.csv
```

Processed dataset size:

**9,994 records**

Important analytical fields include:

- Sales
- Profit
- Region
- Category
- Sub-Category
- Discount
- Product information
- Order information

---

## Analytics Performed

### Overall Business Performance

- Total Sales
- Total Profit
- Profit Margin

### Sales and Profit by Year

- Annual sales trends
- Annual profit trends
- Year-over-year changes

### Regional Performance

- Sales by region
- Profit margin by region

### Category Profitability

- Profit by category
- Profit by sub-category

### Discount and Profitability

- Discount-level profit analysis
- Identification of negative-profit discount levels
- Evidence-based interpretation of discount/profit association

### Loss-Making Products

Identifies products generating negative profit and surfaces significant losses for investigation.

---

## Anomaly Detection

The analytics layer detects grouped business signals such as:

- Significant year-over-year sales changes
- Significant year-over-year profit changes
- Regions with unusually low profit margins
- Loss-making product portfolios
- Discount levels associated with negative total profit

The system treats anomalies as **signals requiring investigation**, not automatic proof of causation.

---

## AI Architecture

```text
Analytics Instructions
        ↓
AI Planning Agent
        ↓
Analysis Executor
        ↓
Recommendation Agent
        ↓
AI Reporting Agent
        ↓
AI Output Validation
```

The AI uses the Gemini API through the Google GenAI Python SDK.

### AI Planning Agent

Implementation:

```text
ai/planner.py
```

The planner receives:

- Analytical instructions
- Structured business metrics
- Detected anomaly signals

It produces a structured analysis plan containing:

- Analysis tasks
- Priorities
- Business questions
- Insight checks
- Report sections

### Analysis Executor

Implementation:

```text
ai/executor.py
```

The executor maps AI-selected tasks to calculated analytical evidence, keeping AI planning separate from deterministic numerical calculations.

### Recommendation Engine

Implementation:

```text
recommendations/recommendation_engine.py
```

The recommendation layer converts detected evidence and anomaly signals into structured business recommendations containing:

- Business area
- Priority
- Recommended action
- Supporting evidence
- Triggering analytical signal

### AI Recommendation Agent

Implementation:

```text
ai/recommendation_agent.py
```

The AI recommendation layer refines deterministic recommendations into clearer business-oriented recommendations while retaining their evidence sources.

### AI Reporting Agent

Implementation:

```text
ai/analyst.py
```

The reporting agent transforms calculated analysis results into:

- Executive Summary
- Key Insights
- Recommendations
- Source Metrics

The AI is instructed not to:

- Invent numerical values
- Change calculated values
- Introduce unsupported facts
- Treat association as causation
- Generate unsupported recommendations

---

## Validation and Reliability

The system uses multiple validation layers.

### Data Validation

Implementation:

```text
validation/validate_data.py
```

Checks include:

- Database availability
- Required table
- Record count
- Required analytical columns

### AI Output Validation

Implementation:

```text
validation/validate_ai_output.py
```

The validator checks:

- Required report sections
- JSON structure
- Source metrics
- Numerical consistency
- Recommendation structure
- Recommendation evidence
- Valid evidence sources

The AI-generated source metrics must match the calculated metrics within the configured tolerance.

---

## Key Business Insights

| Metric | Value |
|---|---:|
| Total Sales | ~$2.30M |
| Total Profit | ~$286.40K |
| Profit Margin | ~12.47% |

### Sales by Region

| Region | Sales |
|---|---:|
| West | ~$0.73M |
| East | ~$0.68M |
| Central | ~$0.50M |
| South | ~$0.39M |

### Profit by Category

| Category | Profit |
|---|---:|
| Technology | ~$145K |
| Office Supplies | ~$122K |
| Furniture | ~$18K |

### Profit Margin by Region

| Region | Profit Margin |
|---|---:|
| West | ~14.94% |
| East | ~13.48% |
| South | ~11.93% |
| Central | ~7.92% |

### Significant Loss-Making Products

- Cubify CubeX 3D Printer Double Head Print: approximately **-$8,879.97**
- Lexmark MX611dhe: approximately **-$4,589.97**

### Discount and Profit

The analysis shows an association between higher discounts and lower or negative profitability. The relationship is not perfectly linear, so the system does not automatically treat discounting alone as proof of causation.

---

## Power BI Dashboard

The project includes:

```text
dashboard/Superstore_Sales_Dashboard.pbix
```

Dashboard components include:

- Total Sales
- Total Profit
- Profit Margin
- Sales and Profit Trend by Year
- Sales by Region
- Profit by Category
- Profit Margin by Region
- Average Discount vs Profit
- Loss-Making Products
- Profit by Sub-Category

Interactive filters:

- Year
- Region

Preview:

```text
reports/dashboard_preview.png
```

---

## Change Detection and Automation

Change detection is implemented in:

```text
state/detect_changes.py
```

The system calculates a SHA-256 hash of:

```text
data/raw/superstore.csv
```

The monitoring system is:

```text
automation/watch_pipeline.py
```

To monitor the dataset continuously:

```powershell
.\.venv\Scripts\python.exe -m automation.watch_pipeline
```

When the dataset changes:

```text
Dataset Changed
      ↓
Pipeline Triggered
      ↓
Database Rebuilt
      ↓
SQL Analysis
      ↓
Metrics
      ↓
Anomaly Detection
      ↓
AI Planning
      ↓
Analysis
      ↓
Recommendations
      ↓
Validation
      ↓
Report + Charts
```

When there is no change, the pipeline avoids unnecessary database rebuilding, SQL execution, AI API calls, report generation, and chart generation.

---

## Generated Outputs

Runtime outputs are generated under:

```text
outputs/
```

Examples:

```text
outputs/
├── business_analysis.json
├── metrics.json
├── anomalies.json
├── analysis_plan.json
├── analysis_results.json
├── recommendations.json
├── ai_recommendations.json
├── final_report.json
└── final_report.md
```

Charts are generated under:

```text
reports/charts/
```

Current chart outputs include:

- profit_by_category.png
- profit_by_subcategory.png
- profit_margin_by_region.png
- sales_by_region.png
- sales_profit_by_year.png

Runtime-generated outputs are excluded from Git version control where appropriate.

---

## Technology Stack

### Data Analytics
- Python
- Pandas
- SQL
- SQLite

### Visualization
- Power BI
- DAX
- Matplotlib

### AI
- Google Gemini
- Google GenAI Python SDK
- Structured JSON generation
- Prompt engineering

### Automation
- Python file monitoring
- SHA-256 change detection
- Pipeline orchestration

### Development
- VS Code
- Git
- GitHub
- Python virtual environment

---

## Project Structure

```text
ecommerce-analytics/
│
├── ai/
│   ├── analyst.py
│   ├── config.py
│   ├── executor.py
│   ├── planner.py
│   └── recommendation_agent.py
│
├── analytics/
│   ├── anomaly_detector.py
│   ├── build_metrics.py
│   └── instruction_loader.py
│
├── automation/
│   └── watch_pipeline.py
│
├── dashboard/
│   └── Superstore_Sales_Dashboard.pbix
│
├── data/
│   ├── raw/
│   │   └── superstore.csv
│   └── processed/
│       └── superstore_clean.csv
│
├── database/
│   ├── load_database.py
│   ├── run_analysis.py
│   └── superstore.db
│
├── instructions/
│   └── analytics_instructions.md
│
├── notebooks/
│   └── 01_data_profiling.ipynb
│
├── recommendations/
│   └── recommendation_engine.py
│
├── reports/
│   ├── Business_Insights.md
│   ├── dashboard_preview.png
│   ├── generate_report.py
│   └── charts/
│       └── generate_charts.py
│
├── sql/
│   └── 01_business_analysis.sql
│
├── state/
│   └── pipeline_state.json
│
├── validation/
│   ├── validate_ai_output.py
│   └── validate_data.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── run_pipeline.py
```

---

## Installation

```bash
git clone https://github.com/RajTripathi7879/ecommerce-analytics.git
cd ecommerce-analytics
python -m venv .venv
```

Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.5-flash-lite
```

A template is provided as:

```text
.env.example
```

The `.env` file is excluded from Git.

**Never commit an actual API key to GitHub.**

---

## Running the Pipeline

```powershell
.\.venv\Scripts\python.exe run_pipeline.py
```

The pipeline performs:

```text
Change Detection
      ↓
Database Loading
      ↓
Data Validation
      ↓
SQL Analysis
      ↓
Metric Construction
      ↓
Anomaly Detection
      ↓
AI Planning
      ↓
Analysis Execution
      ↓
Recommendations
      ↓
AI Reporting
      ↓
AI Validation
      ↓
Report Generation
      ↓
Chart Generation
```

---

## Current Limitations

### Full Recalculation
When new data is detected, the implementation rebuilds the analytical database and recalculates the analysis rather than performing incremental processing.

### AI Dependency
AI planning, recommendation refinement, and reporting depend on access to the configured Gemini model.

### Local Dataset
The current implementation monitors a local CSV file rather than a production database or cloud data source.

### Dashboard Refresh
Power BI remains a separate visualization layer and is not automatically published or refreshed through the Python pipeline.

### Fixed Analytical SQL
The core numerical analyses are predefined SQL queries. The AI selects and interprets available analytical evidence rather than dynamically generating arbitrary SQL.

---

## Skills Demonstrated

### Data Analytics
- Exploratory Data Analysis
- KPI analysis
- Profitability analysis
- Regional analysis
- Category analysis
- Discount analysis
- Business recommendations

### SQL
- Aggregation
- GROUP BY
- Filtering
- Business-oriented analytical queries
- Subqueries
- SQLite

### Python
- Pandas
- JSON processing
- SQLite integration
- Data validation
- File processing
- Automation
- Pipeline orchestration
- Report generation

### Business Intelligence
- Power BI
- DAX
- KPI dashboards
- Interactive filtering
- Business visualization

### AI Engineering
- Gemini API integration
- Prompt engineering
- Structured JSON output
- AI planning
- AI-assisted reporting
- Recommendation refinement
- AI output validation
- Source-of-truth architecture

### Software Engineering
- Modular architecture
- Configuration management
- Validation layers
- Error handling
- Git/GitHub
- Reproducible execution

---

## Engineering Principles

### Separation of Responsibilities

```text
SQL
  → Calculate business metrics

Python
  → Process, validate, detect changes, and orchestrate

AI
  → Plan, interpret, and explain

Power BI
  → Visualize
```

### Deterministic Source of Truth
Business metrics originate from Python and SQL rather than AI-generated calculations.

### Validation Before Reporting
AI-generated outputs are validated against calculated evidence before final reporting.

### Configuration Outside Code
Analytical instructions are maintained separately from the Python implementation.

### Minimal Unnecessary Computation
Change detection prevents unnecessary pipeline execution.

### Modular Design
Each major stage can be tested independently.

---

## End-to-End Workflow

When a new version of the source dataset is added:

```text
1. Detect dataset change
          ↓
2. Rebuild SQLite database
          ↓
3. Validate data
          ↓
4. Execute SQL analysis
          ↓
5. Build structured metrics
          ↓
6. Detect anomalies
          ↓
7. Generate AI analysis plan
          ↓
8. Execute selected analysis
          ↓
9. Generate recommendations
          ↓
10. Refine recommendations with AI
          ↓
11. Generate business insights
          ↓
12. Validate AI output
          ↓
13. Generate final report
          ↓
14. Generate charts
```

---

## Final Architecture

```text
E-COMMERCE DATA
      │
      ▼
CHANGE DETECTION
      │
      ▼
DATA VALIDATION
      │
      ▼
SQL + SQLITE
      │
      ▼
STRUCTURED METRICS
      │
      ├──────────────► ANOMALY DETECTION
      │
      ▼
AI PLANNING AGENT
      │
      ▼
ANALYTICAL EXECUTION
      │
      ▼
RECOMMENDATION ENGINE
      │
      ▼
AI REPORTING
      │
      ▼
AI OUTPUT VALIDATION
      │
   ┌──┴──┐
   ▼     ▼
REPORT  CHARTS
   │     │
   └──┬──┘
      ▼
   POWER BI
```

> **Let deterministic systems calculate the numbers and let AI interpret the numbers.**

---

## Author

**Raj Tripathi**

B.Tech Computer Science  
Big Data Analytics

GitHub: https://github.com/RajTripathi7879/ecommerce-analytics
