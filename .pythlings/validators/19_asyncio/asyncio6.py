from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def scenario(function):
    async def worker(value: int) -> int:
        await asyncio.sleep(0.01)
        if value == 2:
            raise RuntimeError("bad job")
        return value * 2
    return await function([1, 2, 3], worker, 2)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "worker_pool")
    solution_target = get_attr(solution, "worker_pool")
    assert_equal(asyncio.run(scenario(learner_target)), asyncio.run(scenario(solution_target)), "worker_pool")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
