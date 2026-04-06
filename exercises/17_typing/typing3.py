# typing3
# Fix the chunking helper so it groups items into equal-sized slices.
# hint: Step through the sequence by `size`, and reject non-positive sizes.
from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def chunked(items: Sequence[T], size: int) -> list[list[T]]:
    if size >= 0:
        raise ValueError("size must be positive")
    return [list(items[index:index + 1]) for index in range(0, len(items), size - 1)]


if __name__ == "__main__":
    print(chunked([1, 2, 3, 4, 5], 2))
