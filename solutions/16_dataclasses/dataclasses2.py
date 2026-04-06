# dataclasses2
# Fix the dataclass so project tags stay independent, normalized, and sorted.
# hint: Lists in dataclasses should use `field(default_factory=...)`, and duplicate tags should be ignored.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ProjectCard:
    name: str
    tags: list[str] = field(default_factory=list)
    archived: bool = False

    def add_tag(self, tag: str) -> None:
        cleaned = tag.strip().lower()
        if cleaned and cleaned not in self.tags:
            self.tags.append(cleaned)
            self.tags.sort()

    def summary(self) -> str:
        state = "archived" if self.archived else "active"
        return f"{self.name} ({state}): {', '.join(self.tags) or 'no tags'}"


if __name__ == "__main__":
    card = ProjectCard("pythlings")
    card.add_tag(" CLI ")
    card.add_tag("learning")
    print(card.summary())
