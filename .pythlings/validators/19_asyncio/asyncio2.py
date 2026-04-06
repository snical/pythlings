from __future__ import annotations
import asyncio
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
async def scenario(function):
    state = {"running": 0, "max_running": 0}
    async def worker(value: int) -> int:
        state["running"] += 1
        state["max_running"] = max(state["max_running"], state["running"])
        await asyncio.sleep(0.01)
        state["running"] -= 1
        return value * 10
    result = await function([1, 2, 3, 4], 2, worker)
    return result, state["max_running"]
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_result = asyncio.run(scenario(get_attr(learner, "gather_limited")))
    solution_result = asyncio.run(scenario(get_attr(solution, "gather_limited")))
    assert_equal(learner_result, solution_result, "gather_limited")
    try:
        asyncio.run(get_attr(learner, "gather_limited")([1], 0, lambda value: value))
    except ValueError:
        return 0
    except TypeError:
        pass
    raise AssertionError("gather_limited should reject non-positive limits")
if __name__ == "__main__":
    raise SystemExit(main())
