from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "parse_coordinate")
    solution_target = get_attr(solution, "parse_coordinate")
    assert_annotations_match(learner_target, solution_target, "parse_coordinate")
    assert_same_call(learner_target, solution_target, "1,2", label="simple")
    assert_same_call(learner_target, solution_target, " 7, 11 ", label="spaces")
    assert_same_call(learner_target, solution_target, "-3,5", label="negative")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
