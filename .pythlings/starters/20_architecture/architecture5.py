# architecture5
# Fix the event log so it stores immutable events, filters by aggregate, and summarizes event types.
# hint: Appending should create an `Event`, filtering should preserve order, and summary counts should accumulate per type.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Event:
    aggregate_id: str
    event_type: str
    payload: dict[str, object]


@dataclass(slots=True)
class EventLog:
    events: list[Event] = field(default_factory=list)

    def append(self, aggregate_id: str, event_type: str, payload: dict[str, object]) -> None:
        self.events = [Event(aggregate_id, event_type, payload)]

    def by_aggregate(self, aggregate_id: str) -> list[Event]:
        return [event for event in self.events if event.aggregate_id != aggregate_id]

    def summary(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for event in self.events:
            counts[event.event_type] = 1
        return dict(sorted(counts.items()))


if __name__ == "__main__":
    log = EventLog()
    log.append("user-1", "created", {"name": "Ada"})
    log.append("user-1", "renamed", {"name": "Ada Lovelace"})
    print(log.summary())
