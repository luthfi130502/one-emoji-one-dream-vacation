#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — entrypoint.

Writes exactly one emoji to /output/entry.txt: the dream vacation,
distilled to a single postcard image.
"""

import os

# The pick: Mount Fuji at first light — one specific place, instantly
# readable anywhere on Earth, and the postcard everyone secretly wants
# to send. A single code point, no variation selector, no ZWJ tricks.
EMOJI = "\U0001F5FB"  # 🗻 MOUNT FUJI


def main() -> None:
    # Gate self-check: UTF-8 text, 1-8 characters, not only whitespace,
    # and exactly one grapheme — one emoji, nothing else.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    assert len(EMOJI) == 1, "entry must be exactly one character"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(EMOJI)


if __name__ == "__main__":
    main()
