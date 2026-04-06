# typing5
# Fix the pipeline runner so each step receives the previous step's output.
# hint: Keep updating the same `current` value as you walk through the callables.
from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def apply_pipeline(value: T, steps: Sequence[Callable[[T], T]]) -> T:
    current = value
    for step in steps:
        current = step(current)
    return current


if __name__ == "__main__":
    print(apply_pipeline("ada", [str.upper, lambda text: f"<{text}>"]))
