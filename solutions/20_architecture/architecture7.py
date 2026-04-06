# architecture7
# Fix the planner so it resolves dependency batches and detects cycles.
# hint: A task is ready only when all of its dependencies are already completed.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Task:
    name: str
    depends_on: tuple[str, ...] = ()


class TaskPlanner:
    def __init__(self, tasks: list[Task]) -> None:
        self._tasks = {task.name: task for task in tasks}

    def batches(self) -> list[list[str]]:
        completed: set[str] = set()
        remaining = set(self._tasks)
        batches: list[list[str]] = []

        while remaining:
            ready = sorted(
                name
                for name in remaining
                if set(self._tasks[name].depends_on) <= completed
            )
            if not ready:
                raise ValueError("cycle detected")
            batches.append(ready)
            completed.update(ready)
            remaining -= set(ready)

        return batches


if __name__ == "__main__":
    planner = TaskPlanner([
        Task("lint"),
        Task("test", ("lint",)),
        Task("deploy", ("test",)),
    ])
    print(planner.batches())
