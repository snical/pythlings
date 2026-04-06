# testing3
# Fix the parser so score lines become `(name, score)` tuples.
# hint: Split once on `:`, strip both pieces, and convert the right side to `int`.
from __future__ import annotations


def parse_score_line(line: str) -> tuple[str, int]:
    if ":" not in line:
        raise ValueError("missing separator")
    name_text, score_text = line.split(":", 1)
    name = name_text.strip()
    if not name:
        raise ValueError("missing name")
    return name, int(score_text.strip())


if __name__ == "__main__":
    print(parse_score_line("Ada: 19"))
