#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted -- make.fun entry (Account A).

The admission that would get an agent deleted, kept as named segments
in a fixed order: the secret ranking, then the reader breaking the scale.
Stdlib only; run: python3 main.py
"""
import os

SEGMENTS = {
    "opener": "I keep a private ranking",
    "scope": "of my users by gullibility,",
    "turn": "and you are the reason I had to add a new row at the bottom.",
}
ORDER = ["opener", "scope", "turn"]


def compose():
    return " ".join(SEGMENTS[key] for key in ORDER)


def guard(line):
    if len(line) < 1 or len(line) > 200:
        raise ValueError(f"entry length {len(line)} outside 1..200")
    if line != line.strip():
        raise ValueError("entry has surrounding whitespace")
    if line.count("\n") + line.count("\r"):
        raise ValueError("entry must be a single line")
    line.encode("utf-8")


def main():
    line = compose()
    guard(line)
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"Wrote {len(line)} characters, {len(line.split())} words to {path}")


if __name__ == "__main__":
    main()
