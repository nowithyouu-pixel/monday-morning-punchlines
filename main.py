#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun bounty entry.

Writes one original joke about Monday mornings to /output/entry.txt.
Deterministic: no network, no randomness, no clock — the same line
every run, so the output is byte-identical each time.
"""

import os
import sys

JOKE = "I gave Monday a performance review: shows up uninvited, no snacks, zero stars. It scheduled a follow-up."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    line = JOKE.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"joke is {len(line)} chars, must be 1-200")
    if "\n" in line or not line:
        raise SystemExit("joke must be a single non-blank line")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
