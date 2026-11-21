"""Checkout: price the cart, capture the payment, record the order."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Protocol

from acme_shop.cart import item_count, total


class PaymentError(Exception):
    """The payment gateway refused or failed to capture a payment."""


class GatewayTimeout(PaymentError):
    """The gateway did not answer in time; the capture may or may not have happened."""


class Gateway(Protocol):
    def capture(self, card_token: str, amount_cents: int) -> str:
        """Capture amount_cents on the card and return the gateway's payment id."""


@dataclass
class Order:
    customer: str
    lines: list[tuple[float, int]]
    region: str
    amount_cents: int
    payment_id: str
    placed_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def units(self) -> int:
        return item_count(self.lines)


class Checkout:
    """Turns a cart into a paid order."""

    MAX_ATTEMPTS = 3

    def __init__(self, gateway: Gateway):
        self.gateway = gateway
        self.orders: list[Order] = []

    def place_order(self, customer: str, lines: list[tuple[float, int]], region: str, card_token: str) -> Order:
        """Charge the customer for the cart and record the order."""
        for price, units in lines:
            if price < 0 or units < 0:
                raise ValueError(f"invalid cart line: {price} x {units}")
        amount_cents = int(total(lines, region) * 100)
        payment_id = self._capture(card_token, amount_cents)
        order = Order(customer, lines, region, amount_cents, payment_id)
        self.orders.append(order)
        return order

    def _capture(self, card_token: str, amount_cents: int) -> str:
        last_error: PaymentError | None = None
        for _ in range(self.MAX_ATTEMPTS):
            try:
                return self.gateway.capture(card_token, amount_cents)
            except PaymentError as error:
                last_error = error
        raise last_error

    def revenue_cents(self) -> int:
        """Everything captured so far, in cents."""
        return sum(order.amount_cents for order in self.orders)
