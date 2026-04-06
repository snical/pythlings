from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def run(module):
    result_cls = get_attr(module, "BatchResult")
    result = result_cls.from_pairs([("alpha", "ok"), ("beta", "timeout"), ("gamma", "ok"), ("delta", "bad-format")])
    return result.successes, result.errors, result.summary()
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(run(learner), run(solution), "batch result")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
