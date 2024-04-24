"""
Utility functions for the app. Can also be considered as the logic section.
"""

import os
from datetime import datetime

import pytz


def return_time(timezone: str = "Europe/Moscow", prometheus=False) -> str:
    """
    Returns the current time in the given timezone.
    :param timezone: The timezone to get the current time from. (Optional, default: Europe/Moscow)
    :param prometheus: Whether to return the time in Prometheus format. (Optional, default: False)
    :return: The current time in the given timezone.
    """
    if prometheus:
        return f"""
        # HELP current_time_in_{timezone} The current time in {timezone}.
        # TYPE current_time_in_{timezone} gauge
        current_time_in_{timezone} {return_tz_time(timezone)}
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


def get_visits() -> int:
    """
    Gets the number of visits from the file.
    :return: The number of visits.
    """

    filename = os.getenv("VISITS_FILE")
    if not filename:
        raise ValueError("The VISITS_FILE environment variable is not set.")
    # if the file does not exist, create it
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("0")
        return 0

    # read the current number of visits
    with open(filename, "r+", encoding="utf-8") as f:
        visits = f.read()
        if not visits:
            f.write("0")
            return 0
        return int(visits)


def increment_visits():
    """
    Increments the number of visits by 1.
    """

    visits = get_visits()
    visits += 1
    filename = os.getenv("VISITS_FILE")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(visits))


def return_visit_counts() -> str:
    """
    Returns the number of visits to the page.
    :return: The number of visits.
    """
    visits = get_visits()
    return f"""
    <h1>Number of visits: {visits}</h1>
    """
