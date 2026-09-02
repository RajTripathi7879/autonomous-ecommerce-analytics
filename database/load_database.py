import sqlite3
import pandas as pd

csv_path = "../data/processed/superstore_clean.csv"
db_path = "superstore.db"

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)

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