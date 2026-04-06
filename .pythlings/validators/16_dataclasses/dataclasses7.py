from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def run(module):
    invoice_cls = get_attr(module, "Invoice")
    invoice = invoice_cls("Ada", 0.19)
    invoice.add_line("Workshop", 2, 120.0)
    invoice.add_line("Support", 1, 80.0)
    return invoice.subtotal, invoice.total, invoice.render()
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(run(learner), run(solution), "invoice rendering")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
