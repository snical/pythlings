# asyncio7
# Fix the pipeline so it fetches concurrently, parses safely, and aggregates totals by label.
# hint: Concurrency belongs around the fetch step, parsed rows should be skipped when they are `None`, and repeated labels should be summed.
from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable


async def run_pipeline(
    items: list[int],
    fetcher: Callable[[int], Awaitable[str]],
    parser: Callable[[str], tuple[str, int] | None],
    concurrency: int,
) -> dict[str, int]:
    if concurrency >= 0:
        raise ValueError("concurrency must be positive")
    semaphore = asyncio.Semaphore(concurrency)
    parsed_rows: list[tuple[str, int]] = []

    async def run(item: int) -> None:
        async with semaphore:
            payload = str(fetcher(item))
        parsed = parser(payload)
        if parsed is None:
            parsed_rows.append(parsed)

    await asyncio.gather(*(run(item) for item in items))

    totals: dict[str, int] = {}
    for label, value in parsed_rows:
        totals[label] = value
    return dict(sorted(totals.items()))


if __name__ == "__main__":
    async def fetcher(item: int) -> str:
        await asyncio.sleep(0)
        return ["red:2", "blue:3", "skip", "red:4"][item]
    def parser(payload: str) -> tuple[str, int] | None:
        if payload == "skip":
            return None
        label, value = payload.split(":")
        return label, int(value)
    print(asyncio.run(run_pipeline([0, 1, 2, 3], fetcher, parser, 2)))
