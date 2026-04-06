from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def collect(module):
    meeting_cls = get_attr(module, "Meeting")
    items = [meeting_cls.from_string("Review", "10:00-10:30"), meeting_cls.from_string("Standup", "09:15-09:30"), meeting_cls.from_string("Pairing", "09:45-10:15")]
    return [(meeting.title, meeting.duration, meeting.ends_at()) for meeting in sorted(items)]
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(collect(learner), collect(solution), "meeting schedule")
    try:
        get_attr(learner, "Meeting").from_string("Broken", "12:00-11:00")
    except ValueError:
        return 0
    raise AssertionError("learner should reject meetings that end before they start")
if __name__ == "__main__":
    raise SystemExit(main())
