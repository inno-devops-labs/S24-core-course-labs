"""
Utility functions for the app. Can also be considered as the logic section.
"""

from datetime import datetime
import pytz
import os


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

def get_visits() -> int:
    filename = os.getenv("VISITS_FILE")
    if not filename:
        raise ValueError("The VISITS_FILE environment variable is not set.")
    # if the file does not exist, create it
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write("0")
        return 0

    # read the current number of visits
    with open(filename, "r") as f:
        visits = int(f.read())
        return visits
    
def increment_visits():
    visits = get_visits()
    visits += 1
    filename = os.getenv("VISITS_FILE")
    with open(filename, "w") as f:
        f.write(str(visits))

def return_visit_counts() -> str:
    visits = get_visits()
    return f"""
    <h1>Number of visits: {visits}</h1>
    """