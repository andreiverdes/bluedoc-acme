import unittest

from acme_shop.wishlist import Wishlist


class WishlistTest(unittest.TestCase):
    def test_add_and_remove(self):
        wishlist = Wishlist("mia")
        wishlist.add("ACME-001", 49.99)
        wishlist.add("ACME-002", 24.50)
        wishlist.remove("ACME-001")
        self.assertEqual(wishlist.items, [("ACME-002", 24.50)])

    def test_move_to_cart(self):
        wishlist = Wishlist("leo")
        wishlist.add("ACME-004", 9.95)
        self.assertEqual(wishlist.move_to_cart("ACME-004", []), [(9.95, 1)])
        self.assertEqual(wishlist.items, [])


if __name__ == "__main__":
    unittest.main()
