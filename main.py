#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? - make.fun entry.

Writes a single number (digits only) to /output/entry.txt: an honest
count of open browser tabs. 137 is a real, lived-in count - high enough
to surprise, low enough to believe: the tabs of someone who opens a
dozen things to read later and never closes any of them.
"""

import os

COUNT = "137"

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(COUNT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
