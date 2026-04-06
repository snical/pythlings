# asyncio2
# Fix the limited gather so it respects the concurrency cap and preserves input order.
# hint: Use a semaphore around the worker call and store each result at its original index.
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable


async def gather_limited(items: list[int], limit: int, worker: Callable[[int], Awaitable[int]]) -> list[int]:
    if limit <= 0:
        raise ValueError("limit must be positive")
    semaphore = asyncio.Semaphore(limit)
    results = [0] * len(items)

    async def run(index: int, item: int) -> None:
        async with semaphore:
            results[index] = await worker(item)

    await asyncio.gather(*(run(index, item) for index, item in enumerate(items)))
    return results


if __name__ == "__main__":
    async def square(value: int) -> int:
        await asyncio.sleep(0)
        return value * value

    print(asyncio.run(gather_limited([1, 2, 3], 2, square)))
