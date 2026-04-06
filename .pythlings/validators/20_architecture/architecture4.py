from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(container_cls):
    calls = {"db": 0}
    def build_db() -> dict[str, int]:
        calls["db"] += 1
        return {"id": calls["db"]}
    container = container_cls()
    container.register("db", build_db)
    first = container.get("db")
    second = container.get("db")
    duplicate = None
    try:
        container.register("db", build_db)
    except ValueError as error:
        duplicate = str(error)
    missing = None
    try:
        container.get("cache")
    except KeyError as error:
        missing = str(error)
    return first, second, first is second, calls["db"], duplicate, missing
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "ServiceContainer")), scenario(get_attr(solution, "ServiceContainer")), "service container")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
