"""One Line of Earned Pride — entry runner.

Reads the single-line entry from entry.txt next to this file and
prints it exactly once, so the line can be run and judged as-is.
"""

from pathlib import Path


def load_entry() -> str:
    """Return the entry line with surrounding whitespace removed."""
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    return text.strip()


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
