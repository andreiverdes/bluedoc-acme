"""Shipping: a flat rate per parcel, free over a threshold."""
from acme_shop.cart import item_count

FREE_OVER = 50.0      # dollars, before tax
PARCEL_RATE = 6.0     # dollars per parcel
UNITS_PER_PARCEL = 5


def shipping_cost(lines: list[tuple[float, int]]) -> float:
    """What the cart pays to ship."""
    if not lines:
        return 0.0
    subtotal = sum(price * units for price, units in lines)
    if subtotal > FREE_OVER:
        return 0.0
    units = item_count(lines)
    parcels = units // UNITS_PER_PARCEL + 1
    return parcels * PARCEL_RATE
