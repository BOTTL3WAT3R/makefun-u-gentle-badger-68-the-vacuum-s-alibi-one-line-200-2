#!/usr/bin/env python3
"""The Vacuum's Alibi: writes the entry line to /output/entry.txt."""
import os

LINE = (
    "I scanned that spot 14 times and classified it as a protected landmark. "
    "Demolition requires a permit. The permit office is also me, and I denied it."
)


def validate(text):
    """Gate self-check: one line, UTF-8, 1 to 200 characters, not blank."""
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    text.encode("utf-8")


def main():
    validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
