import unittest
from datetime import datetime

from acme_shop.reminders import due_for_reminder


class Reminders(unittest.TestCase):
    def test_first_reminder_after_four_hours(self):
        left = datetime(2026, 11, 21, 9, 0)
        self.assertFalse(due_for_reminder(left, datetime(2026, 11, 21, 12, 59), 0, 2))
        self.assertTrue(due_for_reminder(left, datetime(2026, 11, 21, 13, 0), 0, 2))


if __name__ == "__main__":
    unittest.main()
