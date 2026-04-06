from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_same_call, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "load_config")
    solution_target = get_attr(solution, "load_config")
    rows = ["host = localhost", "  ", "# comment", "port=5432", "host=prod"]
    assert_same_call(learner_target, solution_target, rows, label="config rows")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
