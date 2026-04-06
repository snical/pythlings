# dataclasses3
# Fix the meeting parser so sorting, duration, and end times all work together.
# hint: The ordering should be based on `start_minutes`, not the title, and the meeting must end after it starts.
from __future__ import annotations

from dataclasses import dataclass, field


def to_minutes(clock: str) -> int:
    hours_text, minutes_text = clock.split(":")
    return int(hours_text) * 60 + int(minutes_text)


@dataclass(order=True, slots=True)
class Meeting:
    start_minutes: int
    title: str = field(compare=False)
    duration: int = field(compare=False)

    @classmethod
    def from_string(cls, title: str, window: str) -> "Meeting":
        start_text, end_text = window.split("-")
        start = to_minutes(start_text)
        end = to_minutes(end_text)
        if end <= start:
            raise ValueError("meeting must end after it starts")
        return cls(start, title, end - start)

    def ends_at(self) -> str:
        total = self.start_minutes + self.duration
        return f"{total // 60:02d}:{total % 60:02d}"


if __name__ == "__main__":
    meetings = [Meeting.from_string("Standup", "09:00-09:15"), Meeting.from_string("Retro", "11:00-12:00")]
    print([meeting.title for meeting in sorted(meetings)])
