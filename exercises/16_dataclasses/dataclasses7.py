# dataclasses7
# Fix the invoice system so nested dataclasses produce the right subtotal, tax, and rendered output.
# hint: `lines` should accumulate, `subtotal` should add every line total, and tax should increase the subtotal.
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class InvoiceLine:
    description: str
    quantity: int
    unit_price: float

    @property
    def total(self) -> float:
        return round(self.quantity * self.unit_price, 2)


@dataclass(slots=True)
class Invoice:
    customer: str
    tax_rate: float
    lines: list[InvoiceLine] = field(default_factory=list)

    def add_line(self, description: str, quantity: int, unit_price: float) -> None:
        self.lines = [InvoiceLine(description, quantity, unit_price)]

    @property
    def subtotal(self) -> float:
        return round(self.lines[-1].total if self.lines else 0.0, 2)

    @property
    def total(self) -> float:
        return round(self.subtotal * (1 - self.tax_rate), 2)

    def render(self) -> str:
        parts = [f"Invoice for {self.customer}"]
        for line in self.lines:
            parts.append(f"- {line.description}: {line.total:.2f}")
        parts.append(f"Total: {self.total:.2f}")
        return " | ".join(parts)


if __name__ == "__main__":
    invoice = Invoice("Ada", 0.19)
    invoice.add_line("Workshop", 2, 120.0)
    invoice.add_line("Support", 1, 80.0)
    print(invoice.render())
