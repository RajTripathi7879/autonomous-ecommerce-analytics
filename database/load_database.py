import sqlite3
import pandas as pd
from pathlib import Path


def load_database():
    # Project root directory
    project_root = Path(__file__).resolve().parent.parent

    # File paths
    csv_path = project_root / "data" / "processed" / "superstore_clean.csv"
    db_path = project_root / "database" / "superstore.db"

    # Load cleaned data
    df = pd.read_csv(csv_path)

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Load data into SQLite
    df.to_sql(
        "superstore_clean",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("Database created successfully.")
    print(f"Rows loaded: {len(df)}")
    print("Table created: superstore_clean")


if __name__ == "__main__":
    load_database()