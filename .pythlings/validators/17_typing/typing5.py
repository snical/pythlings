from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_same_call, get_attr, load_module
def add_two(value: int) -> int:
    return value + 2
def double(value: int) -> int:
    return value * 2
def wrap(text: str) -> str:
    return f"<{text}>"
def loud(text: str) -> str:
    return text.upper()
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "apply_pipeline")
    solution_target = get_attr(solution, "apply_pipeline")
    assert_annotations_match(learner_target, solution_target, "apply_pipeline")
    assert_same_call(learner_target, solution_target, 3, [add_two, double], label="numbers")
    assert_same_call(learner_target, solution_target, "ada", [loud, wrap], label="strings")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
