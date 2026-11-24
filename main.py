#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username, one word and nothing else,
to /output/entry.txt for the judge to compare two at a time.
"""

import os

USERNAME = "hupo3661"

# The gate requires UTF-8 text of 1 to 30 characters, not only
# whitespace, a single word with no spaces, no padding, no gloss.
assert 1 <= len(USERNAME) <= 30, "username must be 1-30 characters"
assert USERNAME == USERNAME.strip(), "username must have no padding"
assert not any(ch.isspace() for ch in USERNAME), "username must be one word"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(USERNAME)
    # Verify exactly what the judge will read.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == USERNAME, "entry.txt does not hold the username"


if __name__ == "__main__":
    main()
