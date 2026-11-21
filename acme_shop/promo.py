"""Promo codes: a percentage or a fixed amount off the cart subtotal."""

PROMOS = {
    "SAVE10": ("percent", 0.10),
    "SPRING15": ("percent", 0.15),
    "WELCOME5": ("fixed", 5.0),
}


def apply_promo(subtotal: float, code: str | None) -> float:
    """The subtotal after a promo code; unknown or missing codes change nothing."""
    if not code:
        return subtotal
    promo = PROMOS.get(code)
    if promo is None:
        return subtotal
    kind, amount = promo
    if kind == "percent":
        return subtotal * (1 - amount)
    return max(subtotal - amount, 0.0)
