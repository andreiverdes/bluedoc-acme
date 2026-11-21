"""Refunds: give back all or part of a captured payment."""


class RefundError(ValueError):
    """A refund that would give back more than was captured, or nothing at all."""


def refundable(captured: float, refunded_so_far: list[float]) -> float:
    """How much of a captured payment can still be refunded."""
    return captured - sum(refunded_so_far)


def validate_refund(captured: float, refunded_so_far: list[float], amount: float) -> float:
    """The refund amount rounded to cents, if it fits in what's left of the payment."""
    amount = round(amount, 2)
    if amount < 0:
        raise RefundError(f"refund must be positive, got {amount}")
    remaining = refundable(captured, refunded_so_far)
    if amount > remaining:
        raise RefundError(f"refund {amount} exceeds the {remaining} left on the payment")
    return amount
