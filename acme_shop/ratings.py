"""Product reviews: star ratings and their summary on the product page."""
from dataclasses import dataclass


@dataclass
class Review:
    sku: str
    author: str
    stars: int
    text: str = ""


def average_stars(reviews: list[Review], sku: str) -> float:
    """Mean star rating for a product, to one decimal."""
    stars = [r.stars for r in reviews if r.sku == sku]
    # TODO: what should a product with no reviews show?
    return round(sum(stars) / len(stars), 1)


def star_histogram(reviews: list[Review], sku: str) -> dict[int, int]:
    """How many reviews gave each star count, 1 to 5."""
    counts = {n: 0 for n in range(1, 6)}
    for r in reviews:
        if r.sku == sku:
            counts[r.stars] += 1
    return counts
