from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "parse_score_line")
    solution_target = get_attr(solution, "parse_score_line")
    assert_same_call(learner_target, solution_target, "Ada: 19", label="simple")
    assert_same_call(learner_target, solution_target, "  Lin :  7 ", label="trimmed")
    assert_same_call(learner_target, solution_target, "No separator", label="missing colon")
    assert_same_call(learner_target, solution_target, ": 4", label="missing name")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
