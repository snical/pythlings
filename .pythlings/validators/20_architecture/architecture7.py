from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(planner_cls, task_cls):
    planner = planner_cls([
        task_cls("lint"),
        task_cls("format"),
        task_cls("test", ("lint", "format")),
        task_cls("deploy", ("test",)),
    ])
    cycle_message = None
    try:
        planner_cls([
            task_cls("a", ("b",)),
            task_cls("b", ("a",)),
        ]).batches()
    except ValueError as error:
        cycle_message = str(error)
    return planner.batches(), cycle_message
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(
        scenario(get_attr(learner, "TaskPlanner"), get_attr(learner, "Task")),
        scenario(get_attr(solution, "TaskPlanner"), get_attr(solution, "Task")),
        "task planner",
    )
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
