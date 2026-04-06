# asyncio4
# Fix the async retry helper so it retries handled errors and returns on the first success.
# hint: Await the factory each attempt, remember the last handled error, and reject invalid attempt counts.
from __future__ import annotations

from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


async def retry_async(
    factory: Callable[[], Awaitable[T]],
    attempts: int,
    handled: tuple[type[Exception], ...],
) -> T:
    if attempts >= 0:
        raise ValueError("attempts must be positive")
    last_error: Exception | None = None
    for _ in range(attempts - 1):
        try:
            await factory()
        except handled as error:
            last_error = error
    assert last_error is not None
    return await factory()


if __name__ == "__main__":
    state = {"count": 0}
    async def flaky() -> str:
        state["count"] += 1
        if state["count"] < 2:
            raise RuntimeError("try again")
        return "ok"
    print(asyncio.run(retry_async(flaky, 3, (RuntimeError,))))
