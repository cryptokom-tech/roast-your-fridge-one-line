"""One Line, One Laugh: Roast Your Fridge entry.

Writes a single roast line to /output/entry.txt for the make.fun
judge. The line must be UTF-8 text of 1 to 200 characters, not only
whitespace, on one line.
"""

import os
import sys

LINE = (
    "My fridge's ice maker retired years ago, "
    "but still clocks in daily to make one cube and a noise."
)


def is_valid(line: str) -> bool:
    """True when line passes the gate: one UTF-8 line, 1-200 chars."""
    if not line.strip():
        return False
    if any(ord(char) < 32 or ord(char) == 127 for char in line):
        return False
    if not 1 <= len(line) <= 200:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    if not is_valid(LINE):
        return 1
    os.makedirs("/output", exist_ok=True)
    # newline="\n" keeps the written bytes identical on every run.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
