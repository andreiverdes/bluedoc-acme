import unittest

from acme_shop.tax import tax_rate


class Tax(unittest.TestCase):
    def test_new_regions(self):
        self.assertEqual(tax_rate("TX"), 0.0625)
        self.assertEqual(tax_rate("wa"), 0.065)


if __name__ == "__main__":
    unittest.main()
