# asyncio1
# Fix the async fetch helper so it awaits every request and keeps the original order.
# hint: `asyncio.gather` preserves order when you pass the coroutines in order.
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable


async def fetch_all(ids: list[int], fetcher: Callable[[int], Awaitable[str]]) -> list[str]:
    return list(await asyncio.gather(*(fetcher(item_id) for item_id in ids)))


if __name__ == "__main__":
    async def fake_fetch(item_id: int) -> str:
        await asyncio.sleep(0)
        return f"name-{item_id}"

    print(asyncio.run(fetch_all([1, 2, 3], fake_fetch)))
