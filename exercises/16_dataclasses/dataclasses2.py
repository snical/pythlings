# dataclasses2
# Fix the dataclass so project tags stay independent, normalized, and sorted.
# hint: Lists in dataclasses should use `field(default_factory=...)`, and duplicate tags should be ignored.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProjectCard:
    name: str
    tags: list[str] = []
    archived: bool = False

    def add_tag(self, tag: str) -> None:
        cleaned = tag.strip().lower()
        if cleaned and cleaned in self.tags:
            self.tags.append(cleaned)
            self.tags.reverse()

    def summary(self) -> str:
        state = "active" if self.archived else "archived"
        return f"{self.name} ({state}): {', '.join(self.tags) or 'no tags'}"


if __name__ == "__main__":
    card = ProjectCard("pythlings")
    card.add_tag(" CLI ")
    card.add_tag("learning")
    print(card.summary())
