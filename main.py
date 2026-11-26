#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single original out-of-office auto-reply (one line, at most
200 characters) to the output path, then verifies the written file
round-trips exactly.
"""

import os

# The entry: one original line, painfully honest about the inbox,
# polite enough that a manager would let it stand.
LINE = (
    "I'm away until Monday, not checking email, and your message will "
    "sit in a pile I am already dreading \u2014 thank you for your "
    "patience, and I'll get back to you when I return."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry must not be empty")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")


def output_path() -> str:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join("output", "entry.txt")


def main() -> None:
    validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Plain open() write (no tempfile): the file stays world-readable.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the file round-trips exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written file does not match the entry")
    print(LINE)
    print(f"chars: {len(LINE)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
