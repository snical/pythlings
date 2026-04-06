from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def scenario(function):
    async def fetcher(item: int) -> str:
        await asyncio.sleep({0: 0.02, 1: 0.0, 2: 0.01, 3: 0.0}[item])
        return ["red:2", "blue:3", "skip", "red:4"][item]
    def parser(payload: str) -> tuple[str, int] | None:
        if payload == "skip":
            return None
        label, value = payload.split(":")
        return label, int(value)
    return await function([0, 1, 2, 3], fetcher, parser, 2)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "run_pipeline")
    solution_target = get_attr(solution, "run_pipeline")
    assert_equal(asyncio.run(scenario(learner_target)), asyncio.run(scenario(solution_target)), "run_pipeline")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
