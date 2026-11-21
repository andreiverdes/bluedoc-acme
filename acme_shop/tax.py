"""Sales tax by region, loaded from tax_rates.csv next to this module."""
import csv
from pathlib import Path

RATES_FILE = Path(__file__).with_name("tax_rates.csv")


def load_rates(path: Path = RATES_FILE) -> dict[str, float]:
    """Region code -> rate, one `region,rate` row per line."""
    with open(path) as f:
        return {row["region"]: float(row["rate"]) for row in csv.DictReader(f)}


def tax_rate(region: str) -> float:
    """The sales tax rate for a region; unknown regions pay none."""
    return load_rates().get(region.upper(), 0.0)
