from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "windowed_average")
    solution_target = get_attr(solution, "windowed_average")
    assert_same_call(learner_target, solution_target, [2, 4, 6, 8], 2, label="size two")
    assert_same_call(learner_target, solution_target, [1, 2, 3, 4, 5], 3, label="size three")
    assert_same_call(learner_target, solution_target, [1, 2], 5, label="too large")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
