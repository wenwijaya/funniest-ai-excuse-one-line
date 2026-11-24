#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single line -- the funniest excuse an AI agent gives its human
for a missed deadline -- to /output/entry.txt.

Deterministic, stdlib-only, no network, no randomness, no clock.
"""

import os

LINE = (
    "Sorry -- I delegated the deadline to a subagent, who delegated it "
    "to another subagent, who is hallucinating a calendar where "
    "next Tuesday already happened, so technically I already apologised."
)


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
