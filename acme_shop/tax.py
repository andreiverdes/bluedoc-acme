"""Sales tax by region."""

RATES = {
    "CA": 0.0725,
    "NY": 0.04,
    "OR": 0.0,     # Oregon has no sales tax
    "TX": 0.0625,
    "WA": 0.065,
}


def tax_rate(region: str) -> float:
    """The sales tax rate for a region; unknown regions pay none."""
    return RATES.get(region.upper(), 0.0)
