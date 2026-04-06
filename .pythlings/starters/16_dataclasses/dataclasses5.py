# dataclasses5
# Fix the leaderboard so sorting prefers more solved tasks, then lower penalty, then name.
# hint: The `sort_index` should rank better performers first without calling `sorted(..., reverse=True)`.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(order=True, slots=True)
class LeaderboardEntry:
    sort_index: tuple[int, int, str] = field(init=False, repr=False)
    name: str
    solved: int
    penalty: int

    def __post_init__(self) -> None:
        self.sort_index = (self.solved, -self.penalty, self.name.lower())


def ranking(entries: list[LeaderboardEntry]) -> list[str]:
    return [entry.name for entry in sorted(entries, reverse=True)]


if __name__ == "__main__":
    board = [LeaderboardEntry("Ada", 9, 15), LeaderboardEntry("Lin", 9, 12), LeaderboardEntry("Mina", 8, 10)]
    print(ranking(board))
