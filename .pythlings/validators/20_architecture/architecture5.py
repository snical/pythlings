from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module

def scenario(log_cls):
    log = log_cls()
    payload = {"name": "Ada"}
    log.append("user-1", "created", payload)
    payload["name"] = "Changed outside"
    log.append("user-1", "renamed", {"name": "Ada Lovelace"})
    log.append("user-2", "created", {"name": "Lin"})
    events = [
        (event.aggregate_id, event.event_type, event.payload)
        for event in log.by_aggregate("user-1")
    ]
    return events, log.summary()

def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "EventLog")), scenario(get_attr(solution, "EventLog")), "event log")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
