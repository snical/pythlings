from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(trail_cls):
    trail = trail_cls()
    trail.record("Ada", "create", "report")
    trail.record("Ada", "share", "report")
    trail.record("Lin", "review", "report")
    return trail.by_actor("Ada"), trail.summary()
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "AuditTrail")), scenario(get_attr(solution, "AuditTrail")), "audit trail")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
