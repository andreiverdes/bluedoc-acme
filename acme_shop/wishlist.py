"""Wishlist: products a shopper saved for later."""


class Wishlist:
    def __init__(self, owner: str):
        self.owner = owner
        self.items: list[tuple[str, float]] = []   # (sku, price when saved)

    def add(self, sku: str, price: float) -> None:
        self.items.append((sku, price))

    def remove(self, sku: str) -> None:
        index = [s for s, _ in self.items].index(sku)
        del self.items[index]

    def move_to_cart(self, sku: str, cart: list[tuple[float, int]]) -> list[tuple[float, int]]:
        """Add one unit of a saved item to the cart at its saved price and drop it from the list."""
        price = dict(self.items)[sku]
        self.remove(sku)
        return cart + [(price, 1)]
