#!/usr/bin/env python3
"""Write one short poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the same bytes on every run. No network, no input files.
"""

import os
import sys

POEM = """The Hand That Stops

The kettle sings. My hand hangs still,
the door half-open, key half-turned.
Not every road the map insists on
must be walked. Some power is the pause —
the sentence left unfinished, warm,
the engine idling, choosing not to move —
and call that staying.
"""


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    n = len(text)
    if not 1 <= n <= 280:
        print(f"poem is {n} code points, outside 1..280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({n} characters, {len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
