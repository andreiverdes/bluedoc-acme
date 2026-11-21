import unittest

from acme_shop.checkout import Checkout, GatewayTimeout, PaymentError


class FakeGateway:
    """Idempotent by key. Each scripted step is an error raised before capturing,
    or ("timeout_after_capture", error): capture, then raise as if the reply was lost."""

    def __init__(self, steps: list | None = None):
        self.steps = list(steps or [])
        self.attempts = 0
        self.captures: dict[str, tuple[str, int, str]] = {}   # key -> (card, cents, payment id)

    def capture(self, card_token: str, amount_cents: int, idempotency_key: str) -> str:
        self.attempts += 1
        step = self.steps.pop(0) if self.steps else None
        if isinstance(step, PaymentError):
            raise step
        if idempotency_key not in self.captures:
            payment_id = f"pay_{len(self.captures) + 1}"
            self.captures[idempotency_key] = (card_token, amount_cents, payment_id)
        if isinstance(step, tuple):
            raise step[1]
        return self.captures[idempotency_key][2]

    def charged(self) -> list[tuple[str, int]]:
        return [(card, cents) for card, cents, _ in self.captures.values()]


class CheckoutTest(unittest.TestCase):
    def test_places_order(self):
        gateway = FakeGateway()
        checkout = Checkout(gateway)
        order = checkout.place_order("leo", [(10.0, 2)], "NY", "tok_visa")
        self.assertEqual(order.amount_cents, 2080)
        self.assertEqual(order.payment_id, "pay_1")
        self.assertEqual(order.units, 2)
        self.assertEqual(gateway.charged(), [("tok_visa", 2080)])

    def test_amount_is_rounded_not_truncated(self):
        order = Checkout(FakeGateway()).place_order("mia", [(19.99, 1)], "OR", "tok_visa")
        self.assertEqual(order.amount_cents, 1999)

    def test_retries_after_timeout(self):
        gateway = FakeGateway([GatewayTimeout("slow")])
        order = Checkout(gateway).place_order("mia", [(5.0, 1)], "OR", "tok_visa")
        self.assertEqual(order.payment_id, "pay_1")
        self.assertEqual(gateway.attempts, 2)

    def test_timeout_after_capture_charges_once(self):
        gateway = FakeGateway([("timeout_after_capture", GatewayTimeout("reply lost"))])
        order = Checkout(gateway).place_order("sam", [(5.0, 1)], "OR", "tok_visa")
        self.assertEqual(gateway.attempts, 2)
        self.assertEqual(gateway.charged(), [("tok_visa", 500)])
        self.assertEqual(order.payment_id, "pay_1")

    def test_gives_up_after_three_timeouts(self):
        gateway = FakeGateway([GatewayTimeout("slow")] * 3)
        checkout = Checkout(gateway)
        with self.assertRaises(GatewayTimeout):
            checkout.place_order("sam", [(5.0, 1)], "CA", "tok_visa")
        self.assertEqual(gateway.attempts, 3)
        self.assertEqual(checkout.orders, [])

    def test_decline_is_not_retried(self):
        gateway = FakeGateway([PaymentError("declined")])
        checkout = Checkout(gateway)
        with self.assertRaises(PaymentError):
            checkout.place_order("sam", [(5.0, 1)], "CA", "tok_visa")
        self.assertEqual(gateway.attempts, 1)
        self.assertEqual(checkout.orders, [])

    def test_rejects_negative_lines(self):
        with self.assertRaises(ValueError):
            Checkout(FakeGateway()).place_order("leo", [(5.0, -1)], "CA", "tok_visa")

    def test_revenue(self):
        checkout = Checkout(FakeGateway())
        checkout.place_order("leo", [(10.0, 1)], "OR", "tok_visa")
        checkout.place_order("mia", [(2.5, 2)], "OR", "tok_visa")
        self.assertEqual(checkout.revenue_cents(), 1500)


if __name__ == "__main__":
    unittest.main()
