from __future__ import annotations

import copy
import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, get_type_hints


@dataclass(frozen=True)
class CallOutcome:
    returned: Any = None
    exception_type: type[BaseException] | None = None
    exception_message: str | None = None


def load_module(path: Path, *, label: str) -> ModuleType:
    module_name = f"pythlings_{label}_{path.stem}_{abs(hash(path.resolve()))}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(module_name, None)
        raise
    return module


def get_attr(module: ModuleType, name: str) -> Any:
    if not hasattr(module, name):
        raise AssertionError(f"Expected `{name}` to exist in {module.__file__}.")
    return getattr(module, name)


def clone(value: Any) -> Any:
    return copy.deepcopy(value)


def capture_call(function: Any, *args: Any, **kwargs: Any) -> CallOutcome:
    try:
        return CallOutcome(returned=function(*args, **kwargs))
    except Exception as error:
        return CallOutcome(
            exception_type=type(error),
            exception_message=str(error),
        )


def assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        raise AssertionError(
            f"{label} mismatch. Expected {expected!r}, got {actual!r}."
        )


def assert_same_call(
    learner_function: Any,
    solution_function: Any,
    *args: Any,
    label: str,
    **kwargs: Any,
) -> None:
    learner_outcome = capture_call(
        learner_function,
        *clone(args),
        **clone(kwargs),
    )
    solution_outcome = capture_call(
        solution_function,
        *clone(args),
        **clone(kwargs),
    )
    assert_equal(learner_outcome, solution_outcome, label)


def assert_type_hints(obj: Any, expected: dict[str, Any], label: str) -> None:
    actual = get_type_hints(obj)
    if actual != expected:
        raise AssertionError(
            f"{label} type hints mismatch. Expected {expected!r}, got {actual!r}."
        )


def assert_annotations_match(learner_obj: Any, solution_obj: Any, label: str) -> None:
    learner_annotations = getattr(learner_obj, "__annotations__", {})
    solution_annotations = getattr(solution_obj, "__annotations__", {})
    if learner_annotations != solution_annotations:
        raise AssertionError(
            f"{label} annotations mismatch. Expected {solution_annotations!r}, got {learner_annotations!r}."
        )
