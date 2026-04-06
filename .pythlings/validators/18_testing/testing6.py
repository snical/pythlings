from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def successful_run(function):
    calls = {"count": 0}
    def flaky() -> str:
        calls["count"] += 1
        if calls["count"] < 3:
            raise RuntimeError("try again")
        return "ok"
    return function(flaky, 4, (RuntimeError,)), calls["count"]
def failing_run(function):
    calls = {"count": 0}
    def always_bad() -> str:
        calls["count"] += 1
        raise RuntimeError("boom")
    try:
        function(always_bad, 2, (RuntimeError,))
    except RuntimeError as error:
        return str(error), calls["count"]
    return "no-error", calls["count"]
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "retry")
    solution_target = get_attr(solution, "retry")
    assert_equal(successful_run(learner_target), successful_run(solution_target), "successful retry")
    assert_equal(failing_run(learner_target), failing_run(solution_target), "failing retry")
    try:
        learner_target(lambda: "ok", 0, (RuntimeError,))
    except ValueError:
        return 0
    raise AssertionError("retry should reject attempts <= 0")
if __name__ == "__main__":
    raise SystemExit(main())
