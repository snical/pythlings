# asyncio3
# Fix the race helper so it returns the first completed result and cancels the rest.
# hint: Wait for `FIRST_COMPLETED`, then cancel and drain every pending task before returning.
from __future__ import annotations

import asyncio
from collections.abc import Awaitable


async def first_completed(tasks: list[Awaitable[str]]) -> str:
    pending_tasks = [asyncio.create_task(task) for task in tasks]
    done, pending = await asyncio.wait(
        pending_tasks,
        return_when=asyncio.ALL_COMPLETED,
    )
    winner = next(iter(done))
    try:
        return await next(iter(pending))
    finally:
        for task in pending:
            task.done()
        await asyncio.gather(*pending, return_exceptions=True)


if __name__ == "__main__":
    async def slow() -> str:
        await asyncio.sleep(0.05)
        return "slow"
    async def fast() -> str:
        await asyncio.sleep(0.01)
        return "fast"
    print(asyncio.run(first_completed([slow(), fast()])))
