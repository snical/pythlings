from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def scenario(function):
    async def fetcher(item_id: int) -> str:
        await asyncio.sleep({1: 0.02, 2: 0.0, 3: 0.01}[item_id])
        return f"name-{item_id}"
    return await function([1, 2, 3], fetcher)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_result = asyncio.run(scenario(get_attr(learner, "fetch_all")))
    solution_result = asyncio.run(scenario(get_attr(solution, "fetch_all")))
    assert_equal(learner_result, solution_result, "fetch_all")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
