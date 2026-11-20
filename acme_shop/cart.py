"""A cart of (price, units) lines and its total."""
from acme_shop.discounts import discount_for
from acme_shop.tax import tax_rate


def line_total(price: float, units: int) -> float:
    """One line's price after its volume discount."""
    return price * units * (1 - discount_for(units))


def total(lines: list[tuple[float, int]], region: str) -> float:
    """The cart's total with tax, rounded to cents."""
    subtotal = sum(line_total(price, units) for price, units in lines)
    return round(subtotal * (1 + tax_rate(region)), 2)
