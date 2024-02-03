from datetime import datetime
from flask import url_for
import pytz


def return_index() -> str:
    return f"""
    <h1>Index Page</h1>
    Available routes:
    <ul>
    <li><a href={url_for('show_time')}>Show Moscow Time</a></li>
    </ul>
    """


def return_time(timezone: str = "Europe/Moscow") -> str:
    return f"""
    <h1>Current time in Moscow: {return_tz_time(timezone)}</h1>
    """


def return_tz_time(timezone) -> str:
    return datetime.now(pytz.timezone(timezone)).strftime("%H:%M (%I:%M %p)")
