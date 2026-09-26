import hashlib
import subprocess
import sys
import time
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "superstore.csv"

CHECK_INTERVAL_SECONDS = 30


def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def run_pipeline():
    print("\n" + "=" * 60)
    print("DATASET CHANGE DETECTED")
    print("=" * 60)
    print("Starting autonomous analytics pipeline...")

    result = subprocess.run(
        [sys.executable, "run_pipeline.py"],
        cwd=PROJECT_ROOT
    )

    if result.returncode == 0:
        print("\n✓ Pipeline completed successfully.")
    else:
        print(
            f"\n❌ Pipeline failed with exit code "
            f"{result.returncode}."
        )


def watch_dataset():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}"
        )

    last_hash = calculate_file_hash(DATASET_PATH)

    print("=" * 60)
    print("AUTONOMOUS DATASET WATCHER")
    print("=" * 60)
    print(f"Watching: {DATASET_PATH}")
    print(
        f"Checking every "
        f"{CHECK_INTERVAL_SECONDS} seconds."
    )
    print("Press Ctrl+C to stop.")
    print("=" * 60)

    while True:
        time.sleep(CHECK_INTERVAL_SECONDS)

        current_hash = calculate_file_hash(DATASET_PATH)

        if current_hash != last_hash:
            print("\n✓ Dataset change detected.")

            run_pipeline()

            last_hash = calculate_file_hash(DATASET_PATH)

        else:
            print("No dataset change detected.")


if __name__ == "__main__":
    try:
        watch_dataset()
    except KeyboardInterrupt:
        print("\n\nDataset watcher stopped.")