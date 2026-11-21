"""A cart of (price, units) lines and its total."""
from acme_shop.discounts import discount_for
from acme_shop.promo import apply_promo
from acme_shop.tax import tax_rate


def line_total(price: float, units: int) -> float:
    """One line's price after its volume discount."""
    return price * units * (1 - discount_for(units))


def total(lines: list[tuple[float, int]], region: str, promo: str | None = None) -> float:
    """The cart's total with any promo code and tax, rounded to cents."""
    subtotal = sum(line_total(price, units) for price, units in lines)
    subtotal = apply_promo(subtotal, promo)
    return round(subtotal * (1 + tax_rate(region)), 2)


def item_count(lines: list[tuple[float, int]]) -> int:
    """Units in the cart, across every line."""
    return sum(u for _, u in lines)
