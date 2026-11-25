#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "Earth: stunning views, generous hosts, but the Wi-Fi password is a state secret and the locals queue for everything. Three stars."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
