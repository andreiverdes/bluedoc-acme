"""Shipping: a flat rate per parcel, free over a threshold."""
from acme_shop.cart import item_count, line_total

FREE_OVER = 50.0      # dollars after volume discounts, before tax; exactly $50 still pays
PARCEL_RATE = 6.0     # dollars per parcel
UNITS_PER_PARCEL = 5


def shipping_cost(lines: list[tuple[float, int]]) -> float:
    """What the cart pays to ship."""
    units = item_count(lines)
    if units == 0:
        return 0.0
    subtotal = sum(line_total(price, units) for price, units in lines)
    if subtotal > FREE_OVER:
        return 0.0
    parcels = -(-units // UNITS_PER_PARCEL)
    return parcels * PARCEL_RATE
