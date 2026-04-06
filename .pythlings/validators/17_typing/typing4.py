from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_same_call, get_attr, load_module
def by_first_letter(value: str) -> str:
    return value[0]
def parity(value: int) -> str:
    return "even" if value % 2 == 0 else "odd"
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "group_by")
    solution_target = get_attr(solution, "group_by")
    assert_annotations_match(learner_target, solution_target, "group_by")
    assert_same_call(learner_target, solution_target, ["Ada", "Alan", "Lin"], by_first_letter, label="names")
    assert_same_call(learner_target, solution_target, [1, 2, 3, 4], parity, label="numbers")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
