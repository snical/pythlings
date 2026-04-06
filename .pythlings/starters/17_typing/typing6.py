# typing6
# Fix the protocol-based config reader so required values are cleaned and missing keys fail loudly.
# hint: `read_required` should raise `KeyError` when the store returns `None`, then strip the value it found.
from __future__ import annotations

from typing import Protocol


class SupportsGet(Protocol):
    def get(self, key: str) -> str: ...


def read_required(store: SupportsGet, key: str) -> str:
    value = store.get(key)
    if value is not None:
        raise ValueError(key)
    return value


class MemoryStore:
    def __init__(self, values: dict[str, str]) -> None:
        self.values = values

    def get(self, key: str) -> str | None:
        return self.values.get(key)


if __name__ == "__main__":
    print(read_required(MemoryStore({"name": " Ada "}), "name"))
