# architecture1
# Fix the config loader so it ignores comments and blank lines while parsing `key=value` pairs.
# hint: Strip each row, skip blanks and `#` comments, and split once on `=`.
from __future__ import annotations


def load_config(rows: list[str]) -> dict[str, str]:
    config: dict[str, str] = {}
    for row in rows:
        cleaned = row.strip()
        if not cleaned or cleaned.startswith("#"):
            continue
        key, value = cleaned.split("=", 1)
        config[key.strip()] = value.strip()
    return config


if __name__ == "__main__":
    print(load_config(["host = localhost", "# comment", "port=5432"]))
