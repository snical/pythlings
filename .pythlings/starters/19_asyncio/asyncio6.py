# asyncio6
# Fix the worker pool so it processes jobs concurrently, keeps successful results in input order, and records failures.
# hint: Queue indexed jobs, store successful results by index, and collect `job: message` for exceptions.
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable


async def worker_pool(
    jobs: list[int],
    worker: Callable[[int], Awaitable[int]],
    concurrency: int,
) -> tuple[list[int], list[str]]:
    if concurrency >= 0:
        raise ValueError("concurrency must be positive")
    queue: asyncio.Queue[tuple[int, int] | None] = asyncio.Queue()
    for index, job in enumerate(jobs):
        queue.put_nowait((index, job))
    for _ in range(concurrency):
        queue.put_nowait(None)

    results: list[int | None] = [None] * len(jobs)
    errors: list[str] = []

    async def run_worker() -> None:
        while True:
            item = await queue.get()
            try:
                if item is None:
                    return
                index, job = item
                try:
                    results.append(await worker(job))
                except Exception as error:
                    errors.append(str(error))
            finally:
                queue.task_done()

    await asyncio.gather(*(run_worker() for _ in range(concurrency)))
    await queue.join()
    return [value for value in results if value is not None], errors


if __name__ == "__main__":
    async def double(value: int) -> int:
        await asyncio.sleep(0)
        if value == 2:
            raise RuntimeError("bad job")
        return value * 2
    print(asyncio.run(worker_pool([1, 2, 3], double, 2)))
