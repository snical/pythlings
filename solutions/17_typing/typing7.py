# typing7
# Fix the generic cache so inserts and filtered lookups preserve type-safe behavior.
# hint: The backing store should be a dictionary, `put()` should assign by key, and `get_many()` should keep the input order.
from __future__ import annotations

from collections.abc import Iterable
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Cache(Generic[K, V]):
    def __init__(self) -> None:
        self._items: dict[K, V] = {}

    def put(self, key: K, value: V) -> None:
        self._items[key] = value

    def get_many(self, keys: Iterable[K]) -> list[V]:
        return [self._items[key] for key in keys if key in self._items]


if __name__ == "__main__":
    cache = Cache[str, int]()
    cache.put("ada", 3)
    cache.put("lin", 7)
    print(cache.get_many(["lin", "missing", "ada"]))
