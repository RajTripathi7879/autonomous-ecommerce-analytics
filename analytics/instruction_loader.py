from pathlib import Path


def load_analytics_instructions():
    # Project root directory
    project_root = Path(__file__).resolve().parent.parent

    instructions_file = (
        project_root
        / "instructions"
        / "analytics_instructions.md"
    )

    if not instructions_file.exists():
        raise FileNotFoundError(
            f"Instructions file not found: {instructions_file}"
        )

    with open(instructions_file, "r", encoding="utf-8") as file:
        instructions = file.read()

    if not instructions.strip():
        raise ValueError("Analytics instructions file is empty.")

    return instructions


if __name__ == "__main__":
    instructions = load_analytics_instructions()

    print("=" * 50)
    print("ANALYTICS INSTRUCTIONS LOADED")
    print("=" * 50)

    print(f"Characters loaded: {len(instructions)}")
    print(f"Lines loaded: {len(instructions.splitlines())}")

    print("\nInstructions loaded successfully.")