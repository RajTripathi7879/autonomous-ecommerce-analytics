# Autonomous E-Commerce Analytics System

An AI-assisted autonomous analytics system that transforms e-commerce transaction data into business insights, recommendations, reports, and visualizations with minimal manual intervention.

The project started as a traditional **Python + SQL + Power BI e-commerce analytics project** and was extended into an automated analytics pipeline capable of detecting dataset changes, rebuilding the analytical layer, generating an AI analysis plan, producing evidence-based business insights, validating AI outputs, and refreshing reports and charts.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objective](#business-objective)
- [What Makes This Project Different](#what-makes-this-project-different)
- [System Architecture](#system-architecture)
- [Autonomous Pipeline](#autonomous-pipeline)
- [Core Design Principle](#core-design-principle)
- [Dataset](#dataset)
- [Analytics Performed](#analytics-performed)
- [Power BI Dashboard](#power-bi-dashboard)
- [Key Business Insights](#key-business-insights)
- [AI Architecture](#ai-architecture)
- [AI Planning Agent](#ai-planning-agent)
- [AI Reporting Agent](#ai-reporting-agent)
- [Validation and Reliability](#validation-and-reliability)
- [Change Detection and Automation](#change-detection-and-automation)
- [Generated Outputs](#generated-outputs)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Environment Configuration](#environment-configuration)
- [Running the Pipeline](#running-the-pipeline)
- [Automatic Dataset Monitoring](#automatic-dataset-monitoring)
- [No-Change Behavior](#no-change-behavior)
- [Project Evolution](#project-evolution)
- [Current Capabilities](#current-capabilities)
- [Current Limitations](#current-limitations)
- [Future Improvements](#future-improvements)
- [Skills Demonstrated](#skills-demonstrated)
- [Engineering Principles](#engineering-principles)
- [End-to-End Workflow](#end-to-end-workflow)
- [Author](#author)

---

## Project Overview

This project analyzes the Superstore e-commerce dataset to identify sales, profitability, regional, category, product, and discount-related business patterns.

The original project used:

- Python
- Pandas
- SQL
- SQLite
- Power BI
- DAX
- Git/GitHub

The project has now been extended with an **AI-assisted autonomous analytics pipeline**.

Instead of manually executing each analytical stage whenever the dataset changes, the system can detect a change in the source data and automatically execute the complete workflow.

The pipeline can:

1. Detect changes in the source dataset.
2. Rebuild the SQLite analytical database.
3. Validate the database and required fields.
4. Execute predefined SQL business analyses.
5. Convert SQL results into structured metrics.
6. Load analytical instructions.
7. Generate an AI analysis plan using Gemini.
8. Execute the planned analytical workflow.
9. Generate AI-assisted business insights and recommendations.
10. Validate AI-generated results against calculated metrics.
11. Generate a Markdown business report.
12. Generate refreshed analytical charts.

---

## Business Objective

The system is designed to answer practical business questions such as:

- How are sales and profit changing over time?
- Which regions generate the most sales?
- Which regions have stronger profit margins?
- Which categories contribute most to profitability?
- How is discounting associated with profit?
- Which products generate significant losses?
- Which sub-categories contribute most to profit?
- What areas of the business require attention?
- What recommendations are directly supported by the available evidence?

The goal is to move from:

**Raw Data → Analysis → Business Intelligence → Automated Reporting**

---

## What Makes This Project Different

A traditional analytics workflow might look like:

    Dataset
       ↓
    Python / SQL Analysis
       ↓
    Power BI Dashboard
       ↓
    Manual Interpretation

This project extends that workflow into:

    Dataset
       ↓
    Change Detection
       ↓
    Data Validation
       ↓
    Database Refresh
       ↓
    SQL Analytics
       ↓
    Structured Metrics
       ↓
    AI Planning
       ↓
    Analytical Execution
       ↓
    AI Interpretation
       ↓
    AI Output Validation
       ↓
    Business Report
       ↓
    Charts / Dashboard

The system is therefore not simply a dashboard with an AI chatbot attached.

It combines:

- deterministic analytics
- AI-assisted reasoning
- validation
- automation
- reporting
- business intelligence

---

## System Architecture

    ┌─────────────────────┐
    │  Raw E-Commerce Data │
    │    superstore.csv   │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │   Change Detection  │
    │      SHA-256        │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │   Database Loader   │
    │       Python        │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │       SQLite        │
    │  superstore_clean   │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │     SQL Analysis    │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │  Structured Metrics │
    │        JSON         │
    └──────────┬──────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
    ┌──────────────┐  ┌──────────────────┐
    │ Analytics    │  │ AI Planning Agent│
    │ Instructions │  │      Gemini      │
    └──────────────┘  └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │ Analysis Executor│
                      └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │ AI Reporting     │
                      │ Agent            │
                      └────────┬─────────┘
                               │
                               ▼
                      ┌──────────────────┐
                      │ AI Output        │
                      │ Validation       │
                      └────────┬─────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │ Business     │      │ Analytical   │
             │ Report       │      │ Charts       │
             └──────────────┘      └──────────────┘

---

## Autonomous Pipeline

The complete pipeline is orchestrated by:

    run_pipeline.py

The pipeline performs the following stages:

### 1. Load Analytical Instructions

The system loads:

    instructions/analytics_instructions.md

This defines the analytical objectives and rules that guide the AI.

### 2. Detect Dataset Changes

The system calculates a SHA-256 hash of:

    data/raw/superstore.csv

The hash is compared with the previous pipeline state.

### 3. Rebuild the Database

If the dataset has changed, the processed data is loaded into SQLite.

### 4. Validate the Data

The system verifies that the database, table, records, and required analytical columns exist.

### 5. Execute SQL Analytics

Business analysis queries are executed against the SQLite database.

### 6. Build Structured Metrics

The SQL results are converted into:

    outputs/metrics.json

### 7. Generate an AI Analysis Plan

Gemini receives the analytical instructions and calculated metrics and produces a structured analysis plan.

### 8. Execute the Analysis Plan

The generated plan and calculated metrics are passed to the analysis execution layer.

### 9. Generate Business Insights

The AI reporting agent converts the calculated results into a business-oriented report.

### 10. Validate AI Output

The generated report is checked against the calculated source metrics.

### 11. Generate Final Report

A Markdown report is produced.

### 12. Generate Charts

Analytical charts are generated from the calculated metrics.

---

## Core Design Principle

The central architectural principle is:

> **Python and SQL calculate the facts. AI interprets the facts.**

The system intentionally separates deterministic calculations from AI reasoning.

    SOURCE OF TRUTH
           │
     ┌─────┴─────┐
     │           │
    SQL        Python
     │           │
     └─────┬─────┘
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

The AI does not independently calculate important business metrics from raw transactional records.

This makes the system easier to validate and audit.

---

## Dataset

The project uses the Superstore e-commerce dataset.

Raw dataset:

    data/raw/superstore.csv

Processed dataset:

    data/processed/superstore_clean.csv

The processed dataset contains approximately:

    9,994 records

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

The analytical layer calculates the following business metrics.

### Overall Business Performance

- Total Sales
- Total Profit
- Profit Margin

### Sales and Profit by Year

Used to analyze:

- annual sales trends
- annual profit trends
- changes in business performance

### Sales by Region

Regional comparison of:

- West
- East
- Central
- South

### Profit by Category

Categories include:

- Technology
- Office Supplies
- Furniture

### Profit Margin by Region

Used to compare regional profitability.

### Discount vs Profit

Used to examine the relationship between discounting and profitability.

### Loss-Making Products

Identifies products generating negative profit.

### Profit by Sub-Category

Used to identify stronger and weaker product segments.

---

## Power BI Dashboard

The project includes an interactive Power BI dashboard:

    dashboard/Superstore_Sales_Dashboard.pbix

The dashboard includes:

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

Interactive filters include:

- Year
- Region

Dashboard preview:

    reports/dashboard_preview.png

---

## Key Business Insights

The calculated analysis produced the following results.

### Overall Performance

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

### Loss-Making Products

The analysis identified significant losses from products including:

- Cubify CubeX 3D Printer Double Head Print
- Lexmark MX611dhe

Approximate losses:

| Product | Loss |
|---|---:|
| Cubify CubeX 3D Printer Double Head Print | ~$8,879.97 |
| Lexmark MX611dhe | ~$4,589.97 |

### Discount and Profit

The analysis shows that higher discounts are generally associated with lower or negative profitability.

The relationship is not perfectly linear, so the system treats this as an observed association rather than automatically claiming that discounting alone causes losses.

---

## AI Architecture

The AI layer consists of three main components:

    Analytics Instructions
            │
            ▼
    AI Planning Agent
            │
            ▼
    Analysis Executor
            │
            ▼
    AI Reporting Agent
            │
            ▼
    Validated Business Report

The AI layer uses the Gemini API through the Google GenAI Python SDK.

---

## AI Planning Agent

Implementation:

    ai/planner.py

The planning agent receives:

- analytical instructions
- calculated business metrics

It generates a structured analysis plan containing:

- analysis priorities
- business questions
- insight checks
- report sections

The planner returns structured JSON rather than free-form text.

The planner is responsible for deciding how the available analytical results should be interpreted, not for replacing deterministic SQL calculations.

---

## AI Reporting Agent

Implementation:

    ai/analyst.py

The reporting agent transforms calculated analysis results into:

### Executive Summary

A concise overview of business performance.

### Key Insights

Evidence-based observations from the calculated results.

### Recommendations

Business recommendations directly supported by available evidence.

### Source Metrics

Core metrics used for output validation.

The AI is explicitly instructed not to:

- invent numerical values
- change calculated values
- introduce unsupported facts
- claim causation from simple association
- generate recommendations without evidence

---

## Validation and Reliability

The project contains multiple validation layers.

### Data Validation

Implementation:

    validation/validate_data.py

Checks include:

- database availability
- required table availability
- record count
- required analytical columns

Required fields include:

- Sales
- Profit
- Region
- Category
- Discount

### AI Output Validation

Implementation:

    validation/validate_ai_output.py

The validator checks:

- required report sections
- JSON structure
- source metrics
- numerical consistency
- recommendation evidence
- valid evidence sources

The AI-generated source metrics must match the calculated metrics within the configured tolerance.

This creates a validation boundary between AI interpretation and final reporting.

---

## Change Detection and Automation

Change detection is implemented in:

    state/detect_changes.py

The system calculates a SHA-256 hash of the raw dataset and compares it with the previous stored state.

State is maintained in:

    state/pipeline_state.json

The monitoring system is implemented in:

    automation/watch_pipeline.py

The watcher monitors:

    data/raw/superstore.csv

When the file changes:

    Dataset Changed
          ↓
    Pipeline Triggered
          ↓
    Database Rebuilt
          ↓
    SQL Analysis
          ↓
    Metrics Generated
          ↓
    AI Planning
          ↓
    AI Reporting
          ↓
    Validation
          ↓
    Report + Charts

---

## Generated Outputs

Runtime analytical outputs are generated under:

    outputs/

Examples:

    outputs/
    ├── analysis_plan.json
    ├── analysis_results.json
    ├── business_analysis.json
    ├── final_report.json
    ├── final_report.md
    └── metrics.json

Generated charts are stored under:

    reports/charts/

Current chart outputs include:

- profit_by_category.png
- profit_by_subcategory.png
- profit_margin_by_region.png
- sales_by_region.png
- sales_profit_by_year.png

Generated runtime files are excluded from Git version control.

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

### Artificial Intelligence

- Google Gemini
- Google GenAI Python SDK
- Structured JSON generation

### Automation

- Python file monitoring
- SHA-256 change detection
- Automated pipeline orchestration

### Development

- VS Code
- Git
- GitHub
- Python virtual environment

---

## Project Structure

    ecommerce-analytics/
    │
    ├── ai/
    │   ├── analyst.py
    │   ├── config.py
    │   ├── executor.py
    │   └── planner.py
    │
    ├── analytics/
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

---

## Installation

Clone the repository:

    git clone https://github.com/RajTripathi7879/ecommerce-analytics.git

Move into the project directory:

    cd ecommerce-analytics

Create a virtual environment:

    python -m venv .venv

Install dependencies:

    .\.venv\Scripts\python.exe -m pip install -r requirements.txt

The project dependencies are defined in:

    requirements.txt

---

## Environment Configuration

Create a `.env` file in the project root.

Example:

    GEMINI_API_KEY=your_gemini_api_key_here
    GEMINI_MODEL=gemini-3.5-flash-lite

A template is provided as:

    .env.example

The `.env` file is excluded from Git through `.gitignore`.

Never commit an actual API key to GitHub.

---

## Running the Pipeline

Run the complete autonomous pipeline with:

    .\.venv\Scripts\python.exe run_pipeline.py

The pipeline automatically performs:

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
    AI Planning
           ↓
    Analysis Execution
           ↓
    AI Reporting
           ↓
    AI Validation
           ↓
    Report Generation
           ↓
    Chart Generation

---

## Automatic Dataset Monitoring

To continuously monitor the dataset:

    .\.venv\Scripts\python.exe -m automation.watch_pipeline

The watcher checks:

    data/raw/superstore.csv

for changes.

When a change is detected, the complete pipeline is triggered automatically.

---

## No-Change Behavior

The pipeline avoids unnecessary processing when the dataset has not changed.

If the SHA-256 hash matches the previously recorded state, the system skips the full pipeline.

Example:

    NO NEW DATA DETECTED

This prevents unnecessary:

- database rebuilding
- SQL execution
- AI API calls
- report generation
- chart generation

---

## Project Evolution

### Stage 1: Traditional Analytics

    CSV
     ↓
    Python
     ↓
    SQL
     ↓
    Power BI

### Stage 2: Structured Analytics Pipeline

    CSV
     ↓
    SQLite
     ↓
    SQL Analysis
     ↓
    Structured Metrics
     ↓
    Reports

### Stage 3: AI-Assisted Analytics

    Structured Metrics
     ↓
    AI Planning
     ↓
    AI Interpretation
     ↓
    Business Report

### Stage 4: Autonomous Analytics

    Dataset
     ↓
    Change Detection
     ↓
    Automated Pipeline
     ↓
    AI Planning
     ↓
    Analysis
     ↓
    Validation
     ↓
    Reporting

The current project represents the autonomous analytics stage.

---

## Current Capabilities

The system currently supports:

- automated dataset change detection
- automatic SQLite database rebuilding
- SQL-based business analysis
- structured analytical metrics
- AI-generated analysis planning
- AI-generated business insights
- AI-generated recommendations
- AI output validation
- data validation
- automated Markdown reporting
- automated chart generation
- automatic pipeline triggering
- no-change detection
- reproducible pipeline execution

---

## Current Limitations

### Full Recalculation

When new data is detected, the current implementation rebuilds the analytical database and recalculates the analysis.

It does not currently perform incremental processing.

### AI Dependency

AI planning and reporting depend on access to the configured Gemini model.

### Local Dataset

The current implementation monitors a local CSV file rather than a production database or cloud data source.

### Dashboard Refresh

Power BI remains a separate visualization layer and is not automatically published or refreshed through the Python pipeline.

### Fixed Analytical SQL

The core numerical analyses are predefined SQL queries.

The AI plans and interprets the analysis but does not dynamically generate arbitrary SQL against the database.

---

## Future Improvements

Potential improvements include:

- incremental data processing
- database-backed production ingestion
- cloud-based execution
- automated Power BI dataset refresh
- anomaly detection
- automated data-quality alerts
- trend forecasting
- natural-language business querying
- multi-agent analytical workflows
- email or Slack reporting
- cloud deployment
- historical report comparison
- model evaluation monitoring
- automated executive summaries

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
- GROUP BY analysis
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
- AI output validation
- Source-of-truth architecture

### Automation

- File monitoring
- SHA-256 change detection
- Automated pipeline execution

### Software Engineering

- Modular architecture
- Environment configuration
- Validation layers
- Error handling
- Git/GitHub
- Reproducible execution

---

## Engineering Principles

### Separation of Responsibilities

Each layer has a specific responsibility:

    SQL
    → Calculate business metrics

    Python
    → Process, validate, and orchestrate

    AI
    → Interpret and explain

    Power BI
    → Visualize

### Deterministic Source of Truth

Business metrics originate from Python and SQL rather than AI-generated calculations.

### Validation Before Reporting

AI-generated reports are validated before being treated as final outputs.

### Configuration Outside Code

Analytical instructions are maintained separately from the Python implementation.

### Minimal Unnecessary Computation

Change detection prevents unnecessary pipeline execution.

### Modular Design

Each major stage can be tested independently.

---

## End-to-End Workflow

When a new version of:

    data/raw/superstore.csv

is added, the system can automatically:

    1. Detect the dataset change
            ↓
    2. Rebuild the SQLite database
            ↓
    3. Validate the database
            ↓
    4. Execute SQL business analysis
            ↓
    5. Build structured metrics
            ↓
    6. Load analytical instructions
            ↓
    7. Generate an AI analysis plan
            ↓
    8. Execute the analytical workflow
            ↓
    9. Generate business insights
            ↓
    10. Generate evidence-based recommendations
            ↓
    11. Validate AI output
            ↓
    12. Generate the final business report
            ↓
    13. Generate refreshed analytical charts

The result is an automated analytics workflow that reduces the need for manually rerunning individual scripts whenever the source data changes.

---

## Final Architecture

    E-COMMERCE DATA
           │
           ▼
    CHANGE DETECTION
           │
           ▼
    DATA VALIDATION
           │
           ▼
      SQLITE + SQL
           │
           ▼
    STRUCTURED METRICS
           │
           ▼
    AI PLANNING AGENT
           │
           ▼
    ANALYTICAL EXECUTION
           │
           ▼
    AI REPORTING AGENT
           │
           ▼
    AI OUTPUT VALIDATION
           │
      ┌────┴────┐
      ▼         ▼
    REPORT    CHARTS
      │         │
      └────┬────┘
           ▼
       POWER BI

### Core Idea

> **Let deterministic systems calculate the numbers and let AI interpret the numbers.**

This architecture combines traditional data analytics, business intelligence, AI-assisted reasoning, validation, and automation into a single end-to-end e-commerce analytics system.

---

## Author

**Raj Tripathi**

B.Tech Computer Science  
Big Data Analytics

GitHub: https://github.com/RajTripathi7879/ecommerce-analytics