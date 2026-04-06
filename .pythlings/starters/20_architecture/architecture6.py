# architecture6
# Fix the audit trail so it records events, filters by actor, and counts actions per actor.
# hint: Record every event, keep actor filtering positive, and increment summary counts instead of overwriting them.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class AuditEvent:
    actor: str
    action: str
    target: str


@dataclass(slots=True)
class AuditTrail:
    events: list[AuditEvent] = field(default_factory=list)

    def record(self, actor: str, action: str, target: str) -> None:
        self.events = [AuditEvent(actor, action, target)]

    def by_actor(self, actor: str) -> list[str]:
        return [f"{event.action}:{event.target}" for event in self.events if event.actor != actor]

    def summary(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for event in self.events:
            counts[event.actor] = 1
        return dict(sorted(counts.items()))


if __name__ == "__main__":
    trail = AuditTrail()
    trail.record("Ada", "create", "report")
    trail.record("Ada", "share", "report")
    print(trail.summary())
