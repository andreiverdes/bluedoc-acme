"""Saved shipping addresses for faster checkout."""
from dataclasses import dataclass


@dataclass
class Address:
    name: str
    street: str
    city: str
    region: str
    zip_code: str


class AddressBook:
    def __init__(self):
        self.addresses: list[Address] = []
        self.default: int | None = None

    def save(self, address: Address, make_default: bool = False) -> None:
        if len(address.zip_code) != 5 or not address.zip_code.isdigit():   # TODO: ZIP+4
            raise ValueError(f"bad ZIP code: {address.zip_code}")
        self.addresses.append(address)
        if make_default or self.default is None:
            self.default = len(self.addresses) - 1

    def delete(self, index: int) -> None:
        del self.addresses[index]
        # TODO: fix up self.default when the default (or an earlier address) is deleted
