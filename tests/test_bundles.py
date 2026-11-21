import unittest

from acme_shop.bundles import bundle_discount

PRICES = {"ACME-001": 49.99, "ACME-006": 30.01}


class Bundles(unittest.TestCase):
    def test_complete_bundle(self):
        self.assertAlmostEqual(bundle_discount(["ACME-001", "ACME-006"], PRICES), 12.0)

    def test_incomplete_bundle(self):
        self.assertEqual(bundle_discount(["ACME-001"], PRICES), 0.0)

    def test_two_bundles(self):
        skus = ["ACME-001", "ACME-006", "ACME-001", "ACME-006"]
        self.assertAlmostEqual(bundle_discount(skus, PRICES), 24.0)


if __name__ == "__main__":
    unittest.main()
