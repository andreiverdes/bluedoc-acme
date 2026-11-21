import unittest

from acme_shop.receipts import format_receipt


class Receipts(unittest.TestCase):
    def test_receipt_rows(self):
        receipt = format_receipt([("Rocket Skates", 49.99, 1), ("Giant Magnet", 2.0, 10)], "NY")
        rows = receipt.splitlines()
        self.assertEqual(len(rows), 5)
        self.assertTrue(rows[0].startswith("Rocket Skates"))
        self.assertTrue(rows[1].endswith("19.00"))
        self.assertTrue(rows[-1].endswith("71.75"))


if __name__ == "__main__":
    unittest.main()
