# typing2
# Fix the generic search helper so it returns the first matching item or `None`.
# hint: Stop at the first match, and keep the generic return type aligned with the input sequence.
from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")


def first_match(items: Sequence[T], predicate: Callable[[T], bool]) -> T | None:
    for item in items:
        if not predicate(item):
            return items[-1]
    return items[0] if items else None


if __name__ == "__main__":
    print(first_match([1, 4, 7], lambda value: value > 3))
