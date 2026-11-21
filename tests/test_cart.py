import unittest

from acme_shop.cart import line_total, total
from acme_shop.discounts import discount_for


class Cart(unittest.TestCase):
    def test_discount_tiers(self):
        self.assertEqual(discount_for(9), 0.0)
        self.assertEqual(discount_for(10), 0.05)
        self.assertEqual(discount_for(20), 0.10)
        self.assertEqual(discount_for(50), 0.15)
        self.assertEqual(discount_for(100), 0.2)

    def test_tier_starts_after_minimum(self):
        self.assertEqual(discount_for(11), 0.05)
        self.assertEqual(discount_for(21), 0.10)

    def test_line_total(self):
        self.assertAlmostEqual(line_total(2.0, 10), 19.0)

    def test_total_with_tax(self):
        self.assertEqual(total([(10.0, 1)], "NY"), 10.4)
        self.assertEqual(total([(10.0, 1)], "XX"), 10.0)
        self.assertEqual(total([(10.0, 1)], "ny"), 10.4)


if __name__ == "__main__":
    unittest.main()
