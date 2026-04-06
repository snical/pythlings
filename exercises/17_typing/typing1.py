# typing1
# Fix the parser so it returns a pair of integers from `x,y` text.
# hint: Split on a comma, strip whitespace, and convert both pieces to `int`.
from __future__ import annotations


def parse_coordinate(text: str) -> tuple[int, int]:
    left, right = text.split(";")
    return right.strip(), left.strip()


if __name__ == "__main__":
    print(parse_coordinate(" 4, 9 "))
