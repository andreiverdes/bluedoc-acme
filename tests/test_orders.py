import unittest

from acme_shop.orders import InvalidTransition, advance


class Orders(unittest.TestCase):
    def test_happy_path(self):
        status = "placed"
        for step in ("paid", "shipped", "delivered"):
            status = advance(status, step)
        self.assertEqual(status, "delivered")

    def test_cannot_cancel_after_shipping(self):
        with self.assertRaises(InvalidTransition):
            advance("shipped", "cancelled")


if __name__ == "__main__":
    unittest.main()
