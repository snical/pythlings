# testing7
# Fix the mini test runner so it executes checks in name order and captures failures.
# hint: Sort the check names, run each callable once, and collect `name: message` for every exception.
from __future__ import annotations

from collections.abc import Callable


def run_checks(checks: dict[str, Callable[[], None]]) -> list[str]:
    failures: list[str] = []
    for name in sorted(checks):
        try:
            checks[name]()
        except Exception as error:
            failures.append(f"{name}: {error}")
    return failures


if __name__ == "__main__":
    def ok() -> None:
        return None
    def bad() -> None:
        raise AssertionError("broken")
    print(run_checks({"b": bad, "a": ok}))
