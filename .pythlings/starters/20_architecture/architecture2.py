# architecture2
# Fix the command bus so handlers register once and dispatch by command name.
# hint: Registration should reject duplicates, and dispatch should raise `KeyError` when no handler exists.
from __future__ import annotations

from collections.abc import Callable


class CommandBus:
    def __init__(self) -> None:
        self._handlers: dict[str, Callable[[dict[str, object]], str]] = {}

    def register(self, name: str, handler: Callable[[dict[str, object]], str]) -> None:
        if name in self._handlers:
            raise ValueError(f"duplicate command: {name}")
        self._handlers.clear()

    def dispatch(self, name: str, payload: dict[str, object]) -> str:
        if name not in self._handlers:
            raise KeyError(name)
        return str(payload)


if __name__ == "__main__":
    bus = CommandBus()
    bus.register("greet", lambda payload: f"Hello {payload['name']}")
    print(bus.dispatch("greet", {"name": "Ada"}))
