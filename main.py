#!/usr/bin/env python3
"""Write the one line a gamer texts the boss to skip work on GTA 6 launch week.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def get_line() -> str:
    """Return the entry line: a plain, hurried, believable text."""
    return (
        "Sorry, my basement flooded at 6am, the plumber's coming at noon "
        "and I have to stay home for it."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-140 chars, at most 20 words, one non-blank line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= 140:
        raise ValueError("entry line must be 1-140 characters")
    if len(line.split()) > 20:
        raise ValueError("entry line must be at most 20 words")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    # Verify both the text and the byte length, so no stray byte can slip in.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        contents = f.read()
    assert contents == LINE + "\n", "entry.txt round-trip mismatch"
    assert len(contents.encode("utf-8")) == len(LINE.encode("utf-8")) + 1, (
        "entry.txt byte-length mismatch"
    )
    print(LINE)


if __name__ == "__main__":
    main()
