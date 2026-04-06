# architecture3
# Fix the plugin registry so decorators register factories and build them in name order.
# hint: Keep every factory, reject duplicate plugin names, and instantiate plugins from sorted names.
from __future__ import annotations

from collections.abc import Callable


class PluginRegistry:
    def __init__(self) -> None:
        self._factories: dict[str, Callable[[], object]] = {}

    def plugin(self, name: str) -> Callable[[Callable[[], object]], Callable[[], object]]:
        def decorator(factory: Callable[[], object]) -> Callable[[], object]:
            if name in self._factories:
                raise ValueError(f"duplicate plugin: {name}")
            self._factories[name] = factory
            return factory
        return decorator

    def build_all(self) -> dict[str, object]:
        return {name: self._factories[name]() for name in sorted(self._factories)}


if __name__ == "__main__":
    registry = PluginRegistry()

    @registry.plugin("alpha")
    def build_alpha() -> str:
        return "A"

    print(registry.build_all())
