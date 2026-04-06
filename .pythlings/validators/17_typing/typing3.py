from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "chunked")
    solution_target = get_attr(solution, "chunked")
    assert_annotations_match(learner_target, solution_target, "chunked")
    assert_same_call(learner_target, solution_target, [1, 2, 3, 4, 5], 2, label="ints")
    assert_same_call(learner_target, solution_target, ["a", "b", "c"], 4, label="larger size")
    assert_same_call(learner_target, solution_target, tuple("abcdef"), 3, label="tuple source")
    try:
        learner_target([1, 2], 0)
    except ValueError:
        return 0
    raise AssertionError("chunked should reject non-positive sizes")
if __name__ == "__main__":
    raise SystemExit(main())
