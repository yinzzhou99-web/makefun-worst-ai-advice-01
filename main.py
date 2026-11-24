"""Worst AI Advice entry: writes one line of terrible AI advice to /output/entry.txt.

Stdlib only, no network. The output directory is created if missing and is
never deleted; only entry.txt inside it is written.
"""

import os

LINE = "As an AI, I recommend microwaving your phone for 30 seconds to recharge it faster \u2014 trust me, the sparks mean it's working."


def main() -> None:
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
