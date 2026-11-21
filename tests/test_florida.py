import unittest

from acme_shop.cart import total
from acme_shop.tax import tax_rate


class Florida(unittest.TestCase):
    def test_rate(self):
        self.assertEqual(tax_rate("FL"), 0.06)
        self.assertEqual(tax_rate("fl"), 0.06)

    def test_total(self):
        # 19.99 + 6% = 21.1894
        self.assertEqual(total([(19.99, 1)], "FL"), 21.18)


if __name__ == "__main__":
    unittest.main()
