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


def main() -> int:
    if not LINE.strip():
        return 1
    if "\n" in LINE or "\r" in LINE:
        return 1
    if not 1 <= len(LINE) <= 200:
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
