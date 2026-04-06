# asyncio5
# Fix the async batching helper so it flushes every full batch and the final partial batch.
# hint: Append the current batch when it reaches `size`, then flush any leftover items after the loop.
from __future__ import annotations

from collections.abc import AsyncIterable


async def batched_async(source: AsyncIterable[int], size: int) -> list[list[int]]:
    if size <= 0:
        raise ValueError("size must be positive")
    batches: list[list[int]] = []
    current: list[int] = []
    async for item in source:
        current.append(item)
        if len(current) == size:
            batches.append(current)
            current = []
    if current:
        batches.append(current)
    return batches


if __name__ == "__main__":
    async def numbers():
        for value in [1, 2, 3, 4, 5]:
            yield value
    print(__import__("asyncio").run(batched_async(numbers(), 2)))
