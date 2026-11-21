"""Gift cards: pay part or all of an order from a card balance."""
from dataclasses import dataclass
from datetime import date


class GiftCardExpired(Exception):
    """The card is past its expiry date and can't be used."""


@dataclass
class GiftCard:
    code: str
    balance: float
    expires: date | None = None


def redeem(card: GiftCard, order_total: float, today: date | None = None) -> float:
    """Take what the card can cover from the order; return what is left to pay by other means."""
    today = today or date.today()
    if card.expires is not None and card.expires < today:
        raise GiftCardExpired(f"{card.code} expired on {card.expires}")
    covered = min(card.balance, order_total)
    card.balance -= covered
    return order_total - covered
