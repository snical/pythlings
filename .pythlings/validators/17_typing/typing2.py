from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_same_call, get_attr, load_module
def is_even(value: int) -> bool:
    return value % 2 == 0
def long_name(value: str) -> bool:
    return len(value) > 4
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "first_match")
    solution_target = get_attr(solution, "first_match")
    assert_annotations_match(learner_target, solution_target, "first_match")
    assert_same_call(learner_target, solution_target, [1, 3, 6, 8], is_even, label="numbers")
    assert_same_call(learner_target, solution_target, ["Ada", "Charles", "Lin"], long_name, label="strings")
    assert_same_call(learner_target, solution_target, [], is_even, label="empty")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
