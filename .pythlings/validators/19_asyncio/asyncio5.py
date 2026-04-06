from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def numbers():
    for value in [1, 2, 3, 4, 5]:
        await asyncio.sleep(0)
        yield value
async def scenario(function):
    return await function(numbers(), 2)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_target = get_attr(learner, "batched_async")
    solution_target = get_attr(solution, "batched_async")
    assert_equal(asyncio.run(scenario(learner_target)), asyncio.run(scenario(solution_target)), "batched_async")
    try:
        async def one():
            yield 1
        asyncio.run(learner_target(one(), 0))
    except ValueError:
        return 0
    raise AssertionError("batched_async should reject non-positive sizes")
if __name__ == "__main__":
    raise SystemExit(main())
