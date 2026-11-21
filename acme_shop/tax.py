"""Sales tax by region."""

RATES = {"CA": 0.0725, "FL": 0.06, "NY": 0.04, "OR": 0.0}   # Oregon has no sales tax


def tax_rate(region: str) -> float:
    """The sales tax rate for a region; unknown regions pay none."""
    return RATES.get(region.upper(), 0.0)
