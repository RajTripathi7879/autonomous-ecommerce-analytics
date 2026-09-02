import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "superstore.db"
SQL_PATH = BASE_DIR.parent / "sql" / "01_business_analysis.sql"

conn = sqlite3.connect(DB_PATH)

with open(SQL_PATH, "r", encoding="utf-8") as file:
    sql_script = file.read()

# Remove SQL comment lines
sql_script = "\n".join(
    line for line in sql_script.splitlines()
    if not line.strip().startswith("--")
)

queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]

for i, query in enumerate(queries, start=1):
    print(f"\n{'=' * 60}")
    print(f"QUERY {i}")
    print("=" * 60)

    rows = conn.execute(query).fetchall()

    for row in rows:
        print(row)

conn.close()

print("\nAnalysis completed successfully.")