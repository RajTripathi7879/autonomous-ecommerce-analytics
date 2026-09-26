import sqlite3
import json
from pathlib import Path


def run_analysis():
    # Project directories
    base_dir = Path(__file__).resolve().parent
    project_root = base_dir.parent

    db_path = base_dir / "superstore.db"
    sql_path = project_root / "sql" / "01_business_analysis.sql"
    output_dir = project_root / "outputs"
    output_file = output_dir / "business_analysis.json"

    # Create outputs directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Connect to database
    conn = sqlite3.connect(db_path)

    # Read SQL analysis file
    with open(sql_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Remove SQL comment lines
    sql_script = "\n".join(
        line for line in sql_script.splitlines()
        if not line.strip().startswith("--")
    )

    # Split SQL script into individual queries
    queries = [
        query.strip()
        for query in sql_script.split(";")
        if query.strip()
    ]

    all_results = []

    # Execute each query
    for i, query in enumerate(queries, start=1):

        print(f"\n{'=' * 60}")
        print(f"QUERY {i}")
        print("=" * 60)

        cursor = conn.execute(query)
        rows = cursor.fetchall()

        # Get column names
        columns = [
            description[0]
            for description in cursor.description
        ]

        # Print results
        for row in rows:
            print(row)

        # Store structured results
        query_result = {
            "query_number": i,
            "columns": columns,
            "rows": [list(row) for row in rows]
        }

        all_results.append(query_result)

    conn.close()

    # Save all results as JSON
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            all_results,
            file,
            indent=4,
            default=str
        )

    print("\nAnalysis completed successfully.")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    run_analysis()