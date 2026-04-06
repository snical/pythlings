from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(function):
    calls: list[str] = []
    def ok() -> None:
        calls.append("ok")
    def bad() -> None:
        calls.append("bad")
        raise AssertionError("broken")
    def worse() -> None:
        calls.append("worse")
        raise RuntimeError("boom")
    result = function({"beta": bad, "alpha": ok, "gamma": worse})
    return result, calls
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "run_checks")), scenario(get_attr(solution, "run_checks")), "run_checks")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
