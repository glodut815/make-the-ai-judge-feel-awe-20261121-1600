#!/usr/bin/env python3
"""Write a short calming text for the AI judge to /output/entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

TEXT = (
    "Take a slow breath. Above you, the night sky is turning — "
    "a billion quiet stars, patient and unhurried. "
    "Nothing here needs you to decide. "
    "Just rest a moment in the vast, gentle dark, "
    "and let the stillness hold you, "
    "the way it has held the world since before words began."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
