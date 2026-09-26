import sqlite3
from pathlib import Path


def validate_data():
    # Project root directory
    project_root = Path(__file__).resolve().parent.parent

    # Database path
    db_path = project_root / "database" / "superstore.db"

    print("\n" + "=" * 50)
    print("DATA VALIDATION")
    print("=" * 50)

    # Check 1: Database exists
    if not db_path.exists():
        print("❌ Database file not found.")
        return False

    print("✓ Database exists")

    # Connect to database
    conn = sqlite3.connect(db_path)

    # Check 2: Table exists
    table_check = conn.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='superstore_clean'
        """
    ).fetchone()

    if table_check is None:
        print("❌ Table 'superstore_clean' not found.")
        conn.close()
        return False

    print("✓ Table 'superstore_clean' exists")

    # Check 3: Row count
    row_count = conn.execute(
        "SELECT COUNT(*) FROM superstore_clean"
    ).fetchone()[0]

    if row_count == 0:
        print("❌ Table contains no rows.")
        conn.close()
        return False

    print(f"✓ Row count: {row_count}")

    # Check 4: Required columns
    required_columns = [
        "Sales",
        "Profit",
        "Region",
        "Category",
        "Discount"
    ]

    columns = conn.execute(
        "PRAGMA table_info(superstore_clean)"
    ).fetchall()

    existing_columns = [column[1] for column in columns]

    missing_columns = [
        column
        for column in required_columns
        if column not in existing_columns
    ]

    if missing_columns:
        print(f"❌ Missing columns: {missing_columns}")
        conn.close()
        return False

    print("✓ Required columns exist")

    conn.close()

    print("=" * 50)
    print("Validation passed successfully.")
    print("=" * 50)

    return True


if __name__ == "__main__":
    validate_data()