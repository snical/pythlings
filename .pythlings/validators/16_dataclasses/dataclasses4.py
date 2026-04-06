from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_cls = get_attr(learner, "Package")
    solution_cls = get_attr(solution, "Package")
    learner_pkg = learner_cls(40, 30, 20, 3.5)
    solution_pkg = solution_cls(40, 30, 20, 3.5)
    assert_equal((learner_pkg.volume_cm3, learner_pkg.chargeable_weight), (solution_pkg.volume_cm3, solution_pkg.chargeable_weight), "package totals")
    try:
        learner_cls(0, 10, 10, 1.0)
    except ValueError:
        return 0
    raise AssertionError("learner should reject zero-sized packages")
if __name__ == "__main__":
    raise SystemExit(main())
