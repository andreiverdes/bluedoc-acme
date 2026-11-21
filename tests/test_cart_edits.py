import unittest

from acme_shop.cart import remove_line, set_units


class CartEdits(unittest.TestCase):
    def test_set_units(self):
        self.assertEqual(set_units([(2.0, 1), (3.0, 4)], 1, 6), [(2.0, 1), (3.0, 6)])

    def test_zero_units_drops_line(self):
        self.assertEqual(set_units([(2.0, 1), (3.0, 4)], 0, 0), [(3.0, 4)])

    def test_remove_line(self):
        self.assertEqual(remove_line([(2.0, 1), (3.0, 4)], 1), [(2.0, 1)])


if __name__ == "__main__":
    unittest.main()
