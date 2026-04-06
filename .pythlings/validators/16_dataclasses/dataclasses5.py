from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def run(module):
    entry = get_attr(module, "LeaderboardEntry")
    ranking = get_attr(module, "ranking")
    board = [entry("Ada", 9, 15), entry("Lin", 9, 12), entry("Mina", 8, 10), entry("Zoe", 9, 12)]
    return ranking(board)
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(run(learner), run(solution), "leaderboard order")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
