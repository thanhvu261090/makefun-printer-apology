#!/usr/bin/env python3
"""The Printer Apology — one funny line of apology from an office printer.

Writes the entry to /output/entry.txt (the make.fun program/v1 harness
expects the entry there) and prints it to stdout.
"""

import os

LINE = "Sorry about the pink spreadsheet. My cyan died in 2019 and nobody has checked on me since."


def main():
    print(LINE)
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
