import unittest

from acme_shop.giftcards import GiftCard, redeem


class GiftCards(unittest.TestCase):
    def test_card_covers_part(self):
        card = GiftCard("SAM-25", 25.0)
        self.assertEqual(redeem(card, 40.0), 15.0)
        self.assertEqual(card.balance, 0.0)

    def test_card_covers_all(self):
        card = GiftCard("LEO-50", 50.0)
        self.assertEqual(redeem(card, 30.0), 0.0)
        self.assertEqual(card.balance, 20.0)


if __name__ == "__main__":
    unittest.main()
