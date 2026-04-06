from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def snapshot(item: object) -> tuple[float, int]:
    return (item.subtotal, item.quantity)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    learner_cls = get_attr(learner, "InventoryItem")
    solution_cls = get_attr(solution, "InventoryItem")
    learner_item = learner_cls("Keyboard", 49.99, 2)
    solution_item = solution_cls("Keyboard", 49.99, 2)
    assert_equal(snapshot(learner_item), snapshot(solution_item), "initial state")
    learner_item.restock(3)
    solution_item.restock(3)
    assert_equal(snapshot(learner_item), snapshot(solution_item), "after restock")
    try:
        learner_cls("Mouse", 10.0, 1).restock(-1)
    except ValueError:
        return 0
    raise AssertionError("learner should reject negative restocks")
if __name__ == "__main__":
    raise SystemExit(main())
