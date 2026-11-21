import unittest

from acme_shop.refunds import RefundError, refundable, validate_refund


class Refunds(unittest.TestCase):
    def test_partial_refund(self):
        self.assertEqual(validate_refund(20.0, [], 7.5), 7.5)

    def test_rounds_to_cents(self):
        self.assertEqual(validate_refund(20.0, [], 3.333), 3.33)

    def test_rejects_over_refund(self):
        with self.assertRaises(RefundError):
            validate_refund(20.0, [15.0], 6.0)

    def test_rejects_negative(self):
        with self.assertRaises(RefundError):
            validate_refund(20.0, [], -1.0)

    def test_refundable(self):
        self.assertEqual(refundable(20.0, [5.0, 5.0]), 10.0)


if __name__ == "__main__":
    unittest.main()
