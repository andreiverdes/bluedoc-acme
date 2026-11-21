import unittest

from acme_shop.checkout import Checkout, GatewayTimeout, PaymentError


class FakeGateway:
    def __init__(self, failures: list[PaymentError] | None = None):
        self.failures = list(failures or [])
        self.captures: list[tuple[str, int]] = []

    def capture(self, card_token: str, amount_cents: int) -> str:
        if self.failures:
            raise self.failures.pop(0)
        self.captures.append((card_token, amount_cents))
        return f"pay_{len(self.captures)}"


class CheckoutTest(unittest.TestCase):
    def test_places_order(self):
        gateway = FakeGateway()
        checkout = Checkout(gateway)
        order = checkout.place_order("leo", [(10.0, 2)], "NY", "tok_visa")
        self.assertEqual(order.amount_cents, 2080)
        self.assertEqual(order.payment_id, "pay_1")
        self.assertEqual(order.units, 2)
        self.assertEqual(gateway.captures, [("tok_visa", 2080)])

    def test_retries_after_timeout(self):
        gateway = FakeGateway([GatewayTimeout("slow")])
        checkout = Checkout(gateway)
        order = checkout.place_order("mia", [(5.0, 1)], "OR", "tok_visa")
        self.assertEqual(order.payment_id, "pay_1")

    def test_gives_up_after_three_failures(self):
        gateway = FakeGateway([PaymentError("declined")] * 3)
        checkout = Checkout(gateway)
        with self.assertRaises(PaymentError):
            checkout.place_order("sam", [(5.0, 1)], "CA", "tok_visa")
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
