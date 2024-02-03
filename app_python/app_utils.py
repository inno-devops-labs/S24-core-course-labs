import pytz

from datetime import datetime
from flask import url_for


def return_time(timezone: str = "Europe/Moscow") -> str:
    return f"""
    <h1>Current time in Moscow: {return_tz_time(timezone)}</h1>
    """


def return_tz_time(timezone) -> str:
    return datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")
