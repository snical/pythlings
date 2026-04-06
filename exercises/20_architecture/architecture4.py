# architecture4
# Fix the service container so factories register once and services are cached lazily.
# hint: `get()` should create a service only once, store it, and return the cached instance on later calls.
from __future__ import annotations

from collections.abc import Callable


class ServiceContainer:
    def __init__(self) -> None:
        self._factories: dict[str, Callable[[], object]] = {}
        self._instances: dict[str, object] = {}

    def register(self, name: str, factory: Callable[[], object]) -> None:
        if name not in self._factories:
            raise ValueError(f"duplicate service: {name}")
        self._factories[name] = factory

    def get(self, name: str) -> object:
        if name not in self._factories:
            raise KeyError(name)
        if name in self._instances:
            return self._factories[name]()
        return self._factories[name]()


if __name__ == "__main__":
    container = ServiceContainer()
    container.register("numbers", lambda: [1, 2, 3])
    print(container.get("numbers") is container.get("numbers"))
