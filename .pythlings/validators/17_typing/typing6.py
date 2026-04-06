from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_equal, get_attr, load_module
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "read_required")
    solution_target = get_attr(solution, "read_required")
    assert_annotations_match(learner_target, solution_target, "read_required")
    assert_annotations_match(get_attr(learner, "SupportsGet").get, get_attr(solution, "SupportsGet").get, "SupportsGet.get")
    learner_store = get_attr(learner, "MemoryStore")({"name": " Ada "})
    solution_store = get_attr(solution, "MemoryStore")({"name": " Ada "})
    assert_equal(learner_target(learner_store, "name"), solution_target(solution_store, "name"), "trimmed value")
    try:
        learner_target(learner_store, "missing")
    except KeyError:
        return 0
    raise AssertionError("read_required should raise KeyError for missing entries")
if __name__ == "__main__":
    raise SystemExit(main())
