import unittest

from acme_shop.shipping import shipping_cost


class Shipping(unittest.TestCase):
    def test_free_over_threshold(self):
        self.assertEqual(shipping_cost([(30.0, 2)]), 0.0)

    def test_exactly_threshold_pays(self):
        self.assertEqual(shipping_cost([(10.0, 5)]), 6.0)

    def test_threshold_uses_discounted_subtotal(self):
        # $52 before the 10-unit discount, $49.40 after: not free.
        self.assertEqual(shipping_cost([(5.2, 10)]), 12.0)

    def test_one_parcel(self):
        self.assertEqual(shipping_cost([(4.0, 3)]), 6.0)

    def test_two_parcels(self):
        self.assertEqual(shipping_cost([(1.0, 7)]), 12.0)

    def test_exact_multiples_of_a_parcel(self):
        self.assertEqual(shipping_cost([(1.0, 5)]), 6.0)
        self.assertEqual(shipping_cost([(1.0, 10)]), 12.0)

    def test_empty_cart_ships_free(self):
        self.assertEqual(shipping_cost([]), 0.0)
        self.assertEqual(shipping_cost([(4.0, 0)]), 0.0)


if __name__ == "__main__":
    unittest.main()
