"""Refunds: give back all or part of a captured payment."""
from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


class RefundError(ValueError):
    """A refund that would give back more than was captured, or nothing at all."""


def _cents(amount: float) -> Decimal:
    return Decimal(str(amount)).quantize(CENT, ROUND_HALF_UP)


def _remaining(captured: float, refunded_so_far: list[float]) -> Decimal:
    return _cents(captured) - sum((_cents(r) for r in refunded_so_far), Decimal(0))


def refundable(captured: float, refunded_so_far: list[float]) -> float:
    """How much of a captured payment can still be refunded."""
    return float(_remaining(captured, refunded_so_far))


def validate_refund(captured: float, refunded_so_far: list[float], amount: float) -> float:
    """The refund amount rounded to cents, if it fits in what's left of the payment."""
    cents = _cents(amount)
    if cents <= 0:
        raise RefundError(f"refund must be positive, got {amount}")
    remaining = _remaining(captured, refunded_so_far)
    if cents > remaining:
        raise RefundError(f"refund {cents} exceeds the {remaining} left on the payment")
    return float(cents)
