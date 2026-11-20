"""Sales tax by region."""

RATES = {"CA": 0.0725, "NY": 0.04, "OR": 0.0}


def tax_rate(region: str) -> float:
    """The sales tax rate for a region; unknown regions pay none."""
    return RATES.get(region, 0.0)
