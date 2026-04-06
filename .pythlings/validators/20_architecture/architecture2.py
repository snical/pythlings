from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(bus_cls):
    bus = bus_cls()
    bus.register("greet", lambda payload: f"Hello {payload['name']}")
    bus.register("sum", lambda payload: str(payload["left"] + payload["right"]))
    greeting = bus.dispatch("greet", {"name": "Ada"})
    total = bus.dispatch("sum", {"left": 2, "right": 5})
    duplicate = None
    try:
        bus.register("greet", lambda payload: "ignored")
    except ValueError as error:
        duplicate = str(error)
    missing = None
    try:
        bus.dispatch("missing", {})
    except KeyError as error:
        missing = str(error)
    return greeting, total, duplicate, missing
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "CommandBus")), scenario(get_attr(solution, "CommandBus")), "command bus")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
