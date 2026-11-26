#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

import os

# The joke: a single original line about office life.
JOKE = (
    "My manager said to bring my whole self to work, "
    "so I brought my resignation letter too."
)


def main() -> None:
    # Gate check, mirroring the competition scorer: 1-200 UTF-8 chars.
    if not (1 <= len(JOKE) <= 200) or not JOKE.strip():
        raise ValueError("joke must be 1-200 non-blank characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
