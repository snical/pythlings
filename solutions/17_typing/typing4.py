# typing4
# Fix the grouping helper so every item lands under the right key.
# hint: Reuse the existing bucket for a key instead of replacing it every time.
from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    grouped: dict[K, list[T]] = {}
    for item in items:
        bucket = key(item)
        grouped.setdefault(bucket, []).append(item)
    return grouped


if __name__ == "__main__":
    print(group_by(["Ada", "Lin", "Alan"], key=lambda name: name[0]))
