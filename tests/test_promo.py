import unittest

from acme_shop.cart import total
from acme_shop.promo import apply_promo


class Promo(unittest.TestCase):
    def test_percent_code(self):
        self.assertAlmostEqual(apply_promo(100.0, "SAVE10"), 90.0)

    def test_fixed_code(self):
        self.assertAlmostEqual(apply_promo(20.0, "WELCOME5"), 15.0)

    def test_unknown_code(self):
        self.assertEqual(apply_promo(20.0, "NOPE"), 20.0)
        self.assertEqual(apply_promo(20.0, None), 20.0)

    def test_total_with_promo(self):
        self.assertEqual(total([(10.0, 2)], "NY", promo="SAVE10"), 18.72)


if __name__ == "__main__":
    unittest.main()
