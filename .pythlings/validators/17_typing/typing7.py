from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_annotations_match, assert_equal, get_attr, load_module
def inspect_cache(cache_cls):
    cache = cache_cls[str, int]()
    cache.put("ada", 3)
    cache.put("lin", 7)
    cache.put("ada", 5)
    return cache.get_many(["lin", "missing", "ada"])
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_cls = get_attr(learner, "Cache")
    solution_cls = get_attr(solution, "Cache")
    assert_annotations_match(learner_cls.put, solution_cls.put, "Cache.put")
    assert_annotations_match(learner_cls.get_many, solution_cls.get_many, "Cache.get_many")
    assert_equal(inspect_cache(learner_cls), inspect_cache(solution_cls), "cache behavior")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
