import unittest
from datetime import date

from acme_shop.loyalty import points_for


class Loyalty(unittest.TestCase):
    def test_weekday(self):
        self.assertEqual(points_for(49.99, date(2026, 11, 18)), 50)   # rounds to the nearest dollar

    def test_weekend_doubles(self):
        self.assertEqual(points_for(20.0, date(2026, 11, 21)), 40)


if __name__ == "__main__":
    unittest.main()
