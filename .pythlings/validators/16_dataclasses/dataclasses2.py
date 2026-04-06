from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def build_state(card_cls):
    first = card_cls("pythlings")
    second = card_cls("backend", archived=True)
    for value in (" CLI ", "learning", "cli", ""):
        first.add_tag(value)
    second.add_tag("infra")
    return (first.tags, second.tags, first.summary(), second.summary())
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(build_state(get_attr(learner, "ProjectCard")), build_state(get_attr(solution, "ProjectCard")), "project cards")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
