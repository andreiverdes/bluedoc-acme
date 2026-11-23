"""Plain-text receipts for order confirmation emails."""
from acme_shop.cart import line_total, total
from acme_shop.tax import tax_rate


def format_receipt(lines: list[tuple[str, float, int]], region: str) -> str:
    """A receipt with one row per (name, price, units) line, then subtotal, tax and total."""
    rows = []
    for name, price, units in lines:
        rows.append(f"{name[:20]:<20} {units:>3} x {price:>7.2f} {line_total(price, units):>9.2f}")
    subtotal = sum(line_total(price, units) for _, price, units in lines)
    tax = round(subtotal * tax_rate(region), 2)
    grand_total = total([(price, units) for _, price, units in lines], region)
    rows.append(f"{'Subtotal':<36} {subtotal:>9.2f}")
    rows.append(f"{'Tax (' + region + ')':<36} {tax:>9.2f}")
    rows.append(f"{'Total':<36} {grand_total:>9.2f}")
    return "\n".join(rows)
