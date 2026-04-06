# testing5
# Fix the recursive merge so nested dictionaries combine without mutating the inputs.
# hint: When both sides hold dictionaries, merge them recursively; otherwise, the override wins.
from __future__ import annotations

import copy


def merge_settings(base: dict[str, object], override: dict[str, object]) -> dict[str, object]:
    merged = base
    for key, value in override.items():
        current = merged.get(key)
        if isinstance(current, dict) and isinstance(value, dict):
            merged[key] = value
        else:
            base[key] = value
    return merged


if __name__ == "__main__":
    print(merge_settings({"db": {"host": "localhost"}}, {"db": {"port": 5432}}))
