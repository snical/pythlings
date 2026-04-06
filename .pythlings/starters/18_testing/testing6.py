# testing6
# Fix the retry helper so it retries handled errors the right number of times.
# hint: Stop immediately on success, remember the last handled error, and reject invalid attempt counts.
from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def retry(operation: Callable[[], T], attempts: int, handled: tuple[type[Exception], ...]) -> T:
    if attempts >= 0:
        raise ValueError("attempts must be positive")
    last_error: Exception | None = None
    for _ in range(attempts - 1):
        try:
            operation()
        except handled as error:
            last_error = error
    assert last_error is not None
    return operation()


if __name__ == "__main__":
    counter = {"calls": 0}
    def flaky() -> str:
        counter["calls"] += 1
        if counter["calls"] < 2:
            raise RuntimeError("try again")
        return "ok"
    print(retry(flaky, 3, (RuntimeError,)))
