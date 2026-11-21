import unittest

from acme_shop.ratings import Review, average_stars, star_histogram

REVIEWS = [
    Review("ACME-001", "leo", 5, "Fast!"),
    Review("ACME-001", "mia", 4),
    Review("ACME-002", "sam", 2, "Too strong"),
]


class Ratings(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average_stars(REVIEWS, "ACME-001"), 4.5)

    def test_histogram(self):
        self.assertEqual(star_histogram(REVIEWS, "ACME-001"), {1: 0, 2: 0, 3: 0, 4: 1, 5: 1})


if __name__ == "__main__":
    unittest.main()
