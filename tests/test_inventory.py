import unittest

from acme_shop.inventory import Inventory, OutOfStock


class InventoryTest(unittest.TestCase):
    def test_reserve_reduces_availability(self):
        inventory = Inventory({"ACME-001": 5})
        inventory.reserve("ACME-001", 3)
        self.assertEqual(inventory.available("ACME-001"), 2)

    def test_cannot_overreserve(self):
        inventory = Inventory({"ACME-001": 2})
        with self.assertRaises(OutOfStock):
            inventory.reserve("ACME-001", 3)

    def test_release(self):
        inventory = Inventory({"ACME-001": 5})
        inventory.reserve("ACME-001", 3)
        inventory.release("ACME-001", 3)
        self.assertEqual(inventory.available("ACME-001"), 5)


if __name__ == "__main__":
    unittest.main()
