# testing2
# Fix the batching helper so it keeps order and handles invalid sizes.
# hint: Slice the list in steps of `batch_size`, and reject sizes less than 1.
from __future__ import annotations


def split_batches(items: list[str], batch_size: int) -> list[list[str]]:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return [items[index:index + batch_size] for index in range(0, len(items), batch_size)]


if __name__ == "__main__":
    print(split_batches(["a", "b", "c", "d", "e"], 2))
