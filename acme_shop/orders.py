"""Order status: where an order is between checkout and the customer's door."""

TRANSITIONS = {
    "placed": {"paid", "cancelled"},
    "paid": {"shipped", "cancelled"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
}
# TODO: returns — "delivered" -> "returned" once the refunds flow lands.


class InvalidTransition(Exception):
    """The order can't move from its current status to the requested one."""


def advance(status: str, new_status: str) -> str:
    """The order's next status, if the move is allowed."""
    if new_status not in TRANSITIONS[status]:
        raise InvalidTransition(f"{status} -> {new_status}")
    return new_status
