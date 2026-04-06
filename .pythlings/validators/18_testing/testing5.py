from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def run(function):
    base = {"db": {"host": "localhost", "flags": ["ro"]}, "debug": False}
    override = {"db": {"port": 5432, "flags": ["rw"]}, "debug": True}
    base_before = repr(base)
    override_before = repr(override)
    merged = function(base, override)
    return merged, repr(base), repr(override), base_before, override_before
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_result = run(get_attr(learner, "merge_settings"))
    solution_result = run(get_attr(solution, "merge_settings"))
    assert_equal(learner_result, solution_result, "merge_settings")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
