"""Gift cards: pay part or all of an order from a card balance."""
from dataclasses import dataclass


@dataclass
class GiftCard:
    code: str
    balance: float


def redeem(card: GiftCard, order_total: float) -> float:
    """Take what the card can cover from the order; return what is left to pay by other means."""
    covered = min(card.balance, order_total)
    card.balance -= covered
    return order_total - covered
