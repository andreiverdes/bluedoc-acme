"""Volume discounts: buy more of one item, pay less per unit."""

TIERS = [(50, 0.15), (20, 0.10), (10, 0.05)]   # (minimum units, discount)


def discount_for(units: int) -> float:
    """The discount rate for this many units of one item."""
    for minimum, rate in TIERS:
        if units >= minimum:
            return rate
    return 0.0
