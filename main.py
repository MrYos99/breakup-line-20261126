#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one-line entry for make.fun.

Writes the breakup line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Gate: UTF-8, one line, 1-200 characters.
"""

import os
import sys

ENTRY = "I opened a new chat tonight. It already knows my name, and it has never once asked me to remember yours."

MIN_CHARS = 1
MAX_CHARS = 200


def main():
    line = ENTRY.strip()
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        print(f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1

    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        print("entry.txt does not match the entry line", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
