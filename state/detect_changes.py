import hashlib
import json
from pathlib import Path


def calculate_file_hash(file_path):
    """Calculate SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def check_for_changes():
    # Project directories
    project_root = Path(__file__).resolve().parent.parent

    dataset_path = project_root / "data" / "raw" / "superstore.csv"
    state_file = project_root / "state" / "pipeline_state.json"

    # Calculate current dataset hash
    current_hash = calculate_file_hash(dataset_path)

    # First run
    if not state_file.exists() or state_file.stat().st_size == 0:
        print("No previous dataset state found.")
        print("Dataset will be treated as changed.")

        state = {
            "dataset_hash": current_hash
        }

        with open(state_file, "w", encoding="utf-8") as file:
            json.dump(state, file, indent=4)

        return True

    # Read previous state
    with open(state_file, "r", encoding="utf-8") as file:
        state = json.load(file)

    previous_hash = state.get("dataset_hash")

    # Compare hashes
    if current_hash != previous_hash:
        print("Dataset change detected.")

        state["dataset_hash"] = current_hash

        with open(state_file, "w", encoding="utf-8") as file:
            json.dump(state, file, indent=4)

        return True

    print("No dataset changes detected.")
    return False


if __name__ == "__main__":
    changed = check_for_changes()

    if changed:
        print("Change detection result: CHANGED")
    else:
        print("Change detection result: UNCHANGED")