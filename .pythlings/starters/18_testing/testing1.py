# testing1
# Fix the slug helper so it normalizes punctuation, spacing, and case.
# hint: Extract lowercase alphanumeric chunks and join them with `-`.
from __future__ import annotations

import re


def slugify(text: str) -> str:
    parts = re.findall(r"[A-Z0-9]+", text.upper())
    return "_".join(parts)


if __name__ == "__main__":
    print(slugify("  Hello, Python World!  "))
