"""
Utility functions for the app. Can also be considered as the logic section.
"""

from datetime import datetime
import pytz


def return_time(timezone: str = "Europe/Moscow") -> str:
    """
    Returns the current time in the given timezone.
    :param timezone: The timezone to get the current time from. (Optional, default: Europe/Moscow)
    :return: The current time in the given timezone.
    """
    return f"""
    <h1>Current time in {timezone}: {return_tz_time(timezone)}</h1>
    """


def return_tz_time(timezone) -> str:
    """
    Returns the current time in the given timezone.
    :param timezone: The timezone to get the current time from.
    :return: The current time in the given timezone.
    """
    return datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")
