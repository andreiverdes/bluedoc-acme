"""Loyalty points: one point per whole dollar spent, double on weekends."""
from datetime import date


def points_for(order_total: float, placed_on: date) -> int:
    """Points earned by an order."""
    points = int(order_total)
    if placed_on.weekday() >= 5:   # Saturday or Sunday
        points *= 2
    # TODO: refunds should claw points back
    return points
