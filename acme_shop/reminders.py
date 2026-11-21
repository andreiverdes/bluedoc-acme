"""Abandoned-cart reminders: nudge shoppers who left items behind."""
from datetime import datetime, timedelta

FIRST_REMINDER_AFTER = timedelta(hours=4)
MAX_REMINDERS = 2


def due_for_reminder(last_activity: datetime, now: datetime, reminders_sent: int, cart_size: int) -> bool:
    """Whether to send another reminder for this cart now."""
    # TODO: last_activity comes from the browser in local time; normalize to UTC first
    if reminders_sent > MAX_REMINDERS:
        return False
    wait = FIRST_REMINDER_AFTER * (reminders_sent + 1)
    return now - last_activity >= wait
