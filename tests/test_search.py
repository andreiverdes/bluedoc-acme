import unittest

from acme_shop.search import search


class Search(unittest.TestCase):
    def test_matches_every_word(self):
        self.assertEqual([p.sku for p in search("Rocket")], ["ACME-001", "ACME-005"])
        self.assertEqual([p.sku for p in search("Rocket Sled")], ["ACME-005"])

    def test_ignores_case(self):
        self.assertEqual([p.sku for p in search("rocket SLED")], ["ACME-005"])

    def test_price_ceiling(self):
        self.assertEqual([p.sku for p in search("Rocket", max_price=100)], ["ACME-001"])

    def test_price_ceiling_includes_the_limit(self):
        self.assertEqual([p.sku for p in search("Rocket", max_price=49.99)], ["ACME-001"])

    def test_limit(self):
        self.assertEqual(len(search("", limit=2)), 2)


if __name__ == "__main__":
    unittest.main()
