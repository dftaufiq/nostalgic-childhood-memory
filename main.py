#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory — make.fun entry.

Writes one sentence (256 chars) recalling a childhood memory to
/output/entry.txt. Deterministic: the same line every run.

The line: last day of school each June, Grandma's banana fritters wrapped
in newspaper, the plastic bag fogged with steam — and forty years later no
street-cart fritter ever fogs the bag. Two beats, reveal in the final
clause: the memory cannot be recaptured, and that is the warm ache.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank sentence of 1-280 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if line != line.strip():
        print("ERROR: entry has leading or trailing whitespace", file=sys.stderr)
        sys.exit(1)
    if len(line) > 280:
        print(f"ERROR: entry is {len(line)} chars, over the 280-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "On the last day of school each June, Grandma fried banana fritters "
    "and wrapped two in newspaper for the walk home, the plastic bag "
    "underneath still fogged with steam; I am forty now and I still buy "
    "them from street carts, but none of them ever fog the bag."
)


def main() -> None:
    validate_line(LINE)
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
