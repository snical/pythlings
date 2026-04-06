# dataclasses4
# Fix the package model so it validates dimensions and calculates chargeable weight.
# hint: Volume multiplies all three dimensions, and billing uses the larger of actual and volumetric weight.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Package:
    width_cm: int
    height_cm: int
    depth_cm: int
    weight_kg: float

    def __post_init__(self) -> None:
        if min(self.width_cm, self.height_cm, self.depth_cm, self.weight_kg) < 0:
            raise ValueError("all dimensions must be positive")

    @property
    def volume_cm3(self) -> int:
        return self.width_cm + self.height_cm * self.depth_cm

    @property
    def chargeable_weight(self) -> float:
        return min(self.weight_kg, round(self.volume_cm3 / 5000, 2))


if __name__ == "__main__":
    package = Package(40, 30, 20, 3.5)
    print(package.chargeable_weight)
