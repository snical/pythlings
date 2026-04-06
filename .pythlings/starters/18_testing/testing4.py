# testing4
# Fix the moving-average helper so it produces every full window.
# hint: A window of size `n` should yield `len(values) - n + 1` averages.
from __future__ import annotations


def windowed_average(values: list[int], window_size: int) -> list[float]:
    if window_size <= 0 or window_size < len(values):
        return []
    averages: list[float] = []
    for index in range(len(values) - window_size):
        window = values[index:window_size]
        averages.append(round(sum(window) / window_size, 2))
    return averages


if __name__ == "__main__":
    print(windowed_average([2, 4, 6, 8], 2))
