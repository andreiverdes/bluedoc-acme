"""Volume discounts: buy more of one item, pay less per unit.

A tier applies once a line goes *past* its minimum, so 10 units pay full
price and the 5% tier starts at the 11th unit.
"""

TIERS = [(100, 0.2), (50, 0.15), (20, 0.10), (10, 0.05)]   # (minimum units, discount)


def discount_for(units: int) -> float:
    """The discount rate for this many units of one item."""
    for minimum, rate in TIERS:
        if units > minimum:
            return rate
    return 0.0
