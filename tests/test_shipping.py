import unittest

from acme_shop.shipping import shipping_cost


class Shipping(unittest.TestCase):
    def test_free_over_threshold(self):
        self.assertEqual(shipping_cost([(30.0, 2)]), 0.0)

    def test_one_parcel(self):
        self.assertEqual(shipping_cost([(4.0, 3)]), 6.0)

    def test_two_parcels(self):
        self.assertEqual(shipping_cost([(1.0, 7)]), 12.0)


if __name__ == "__main__":
    unittest.main()
