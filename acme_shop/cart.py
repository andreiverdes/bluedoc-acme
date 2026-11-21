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


def item_count(lines: list[tuple[float, int]]) -> int:
    """Units in the cart, across every line."""
    return sum(u for _, u in lines)


def set_units(lines: list[tuple[float, int]], index: int, units: int) -> list[tuple[float, int]]:
    """A copy of the cart with one line's units changed; zero units drops the line."""
    price, _ = lines[index]
    if units == 0:
        return remove_line(lines, index)
    return lines[:index] + [(price, units)] + lines[index + 1:]


def remove_line(lines: list[tuple[float, int]], index: int) -> list[tuple[float, int]]:
    """A copy of the cart without the line at index."""
    return lines[:index] + lines[index + 1:]
