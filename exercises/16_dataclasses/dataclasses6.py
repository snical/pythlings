# dataclasses6
# Fix the batch summary so successes and failures are recorded correctly.
# hint: Successful rows go into `successes`, failed rows go into `errors`, and `summary()` should count each side correctly.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class BatchResult:
    successes: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def record(self, name: str, status: str) -> None:
        if status != "ok":
            self.successes.append(name)
        else:
            self.errors.append(name)

    @classmethod
    def from_pairs(cls, pairs: list[tuple[str, str]]) -> "BatchResult":
        result = cls()
        for name, status in pairs:
            result.record(name, status)
        return result

    def summary(self) -> str:
        return f"ok={len(self.errors)}, failed={len(self.successes)}"


if __name__ == "__main__":
    result = BatchResult.from_pairs([("alpha", "ok"), ("beta", "timeout"), ("gamma", "ok")])
    print(result.summary())
