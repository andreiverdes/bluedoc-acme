"""Bundles: buy every item in a set together and pay less."""

BUNDLES = {
    "speed-kit": ({"ACME-001", "ACME-006"}, 0.15),   # Rocket Skates + Crash Helmet
}


def bundle_discount(skus: list[str], prices: dict[str, float]) -> float:
    """Dollars off for every complete bundle in the cart."""
    off = 0.0
    for members, rate in BUNDLES.values():
        if members <= set(skus):
            off += rate * sum(prices[sku] for sku in members)
    # TODO: a cart with two of each should get the bundle twice
    return off
