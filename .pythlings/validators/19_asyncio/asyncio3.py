from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def scenario(function):
    cancelled: list[str] = []
    async def fast() -> str:
        await asyncio.sleep(0.01)
        return "fast"
    async def slow(name: str) -> str:
        try:
            await asyncio.sleep(0.05)
            return name
        except asyncio.CancelledError:
            cancelled.append(name)
            raise
    result = await function([slow("slow-1"), fast(), slow("slow-2")])
    await asyncio.sleep(0)
    return result, sorted(cancelled)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_result = asyncio.run(scenario(get_attr(learner, "first_completed")))
    solution_result = asyncio.run(scenario(get_attr(solution, "first_completed")))
    assert_equal(learner_result, solution_result, "first_completed")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
