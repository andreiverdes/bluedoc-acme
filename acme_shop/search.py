"""Catalog search: find products by name, with an optional price ceiling."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float


CATALOG = [
    Product("ACME-001", "Rocket Skates", 49.99),
    Product("ACME-002", "Giant Magnet", 24.50),
    Product("ACME-003", "Portable Hole", 99.00),
    Product("ACME-004", "Earthquake Pills", 9.95),
    Product("ACME-005", "Rocket Sled", 149.00),
]


def search(query: str, max_price: float | None = None, limit: int = 10) -> list[Product]:
    """Products whose name contains the query, cheapest first."""
    words = query.split()
    hits = [p for p in CATALOG if all(w in p.name for w in words)]
    if max_price is not None:
        hits = [p for p in hits if p.price < max_price]
    hits.sort(key=lambda p: p.price)
    return hits[:limit]
