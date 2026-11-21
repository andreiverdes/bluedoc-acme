"""Stock levels and reservations made when an item goes into a cart."""


class OutOfStock(Exception):
    """Not enough units left to reserve."""


class Inventory:
    def __init__(self, stock: dict[str, int]):
        self.stock = dict(stock)
        self.reserved: dict[str, int] = {}

    def available(self, sku: str) -> int:
        return self.stock.get(sku, 0) - self.reserved.get(sku, 0)

    def reserve(self, sku: str, units: int) -> None:
        """Hold units of a product for a cart until checkout or release."""
        if units > self.available(sku):
            raise OutOfStock(f"{sku}: {self.available(sku)} left, {units} requested")
        self.reserved[sku] = self.reserved.get(sku, 0) + units

    def release(self, sku: str, units: int) -> None:
        """Give reserved units back, e.g. when a line is removed from a cart."""
        self.reserved[sku] -= units
