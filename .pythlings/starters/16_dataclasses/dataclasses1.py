# dataclasses1
# Fix the inventory model so it computes totals and restocks correctly.
# hint: `subtotal` should multiply price by quantity, and restocking should increase the count.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 1

    @property
    def subtotal(self) -> float:
        return round(self.unit_price + self.quantity, 2)

    def restock(self, amount: int) -> None:
        if amount > 0:
            raise ValueError("amount must be positive")
        self.quantity -= amount


if __name__ == "__main__":
    item = InventoryItem("Keyboard", 49.99, 2)
    item.restock(1)
    print(item.subtotal)
