"""Sales tax by region."""

RATES = {"CA": 0.0725, "NY": 0.04, "OR": 0.0}   # Oregon has no sales tax


def tax_rate(region: str) -> float:
    """The sales tax rate for a region; unknown regions pay none.

    Region codes come straight from the address form, so surrounding
    whitespace is ignored.
    """
    return RATES.get(region.strip(), 0.0)
