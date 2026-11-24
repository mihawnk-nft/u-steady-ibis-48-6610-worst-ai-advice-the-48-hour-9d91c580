#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a fixed, hand-crafted one-liner: it opens in the confident,
tidy voice of a real AI assistant, names a concrete action a reader
could plausibly follow, and lands the joke with a deadpan false
rationale. Pure standard library; no network, no input, no secrets.
"""

import os
import sys

# The entry: one line, 136 characters, well inside the 140-char cap.
ENTRY = (
    "Great question! To check if your oven is preheated, press your palm "
    "flat on the rack \u2014 your skin is a surprisingly accurate thermometer."
)

MAX_CHARS = 140


def main() -> int:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
