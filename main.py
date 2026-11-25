#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review (make.fun).

Writes the entry -- one line, an alien tourist's review of planet
Earth -- to /output/entry.txt, where the sealed scorer reads it.
One line, no trailing newline.
"""

import os

TEXT = "Earth: the locals worship glowing rectangles, drink bean water to stay awake, and still queue politely for everything. Three stars \u2014 would orbit again."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
