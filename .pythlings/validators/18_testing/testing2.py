from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "split_batches")
    solution_target = get_attr(solution, "split_batches")
    assert_same_call(learner_target, solution_target, ["a", "b", "c", "d", "e"], 2, label="odd length")
    assert_same_call(learner_target, solution_target, ["a", "b"], 5, label="oversized batch")
    try:
        learner_target(["a"], 0)
    except ValueError:
        return 0
    raise AssertionError("split_batches should reject non-positive sizes")
if __name__ == "__main__":
    raise SystemExit(main())
