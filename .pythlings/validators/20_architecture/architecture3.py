from __future__ import annotations
from pathlib import Path
import sys
from pythlings.validation import assert_equal, get_attr, load_module
def scenario(registry_cls):
    registry = registry_cls()
    @registry.plugin("beta")
    def build_beta() -> str:
        return "B"
    @registry.plugin("alpha")
    def build_alpha() -> str:
        return "A"
    duplicate = None
    try:
        @registry.plugin("alpha")
        def build_again() -> str:
            return "X"
    except ValueError as error:
        duplicate = str(error)
    return registry.build_all(), duplicate
def main() -> int:
    learner = load_module(Path(sys.argv[1]), label="learner")
    solution = load_module(Path(sys.argv[2]), label="solution")
    assert_equal(scenario(get_attr(learner, "PluginRegistry")), scenario(get_attr(solution, "PluginRegistry")), "plugin registry")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
