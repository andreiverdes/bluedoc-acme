"""Shipping: free over a threshold, else a flat fee."""
FREE_OVER = 50.0
FLAT = 4.99


def shipping(subtotal: float) -> float:
    """Shipping for a cart with this subtotal."""
    if subtotal > FREE_OVER:
        return FLAT
    return 0.0
