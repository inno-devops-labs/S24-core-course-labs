"""
Util functions of the app
"""
import os
from datetime import datetime, timezone, timedelta


def get_moscow_time():
    """Return: moscow time in format %Y-%m-%d %H:%M:%S"""
    moscow_tz = timezone(timedelta(hours=3))  # Moscow Time Zone UTC+3
    current_utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    moscow_time = current_utc_time.astimezone(moscow_tz)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')


def increase_num_of_visits():
    """write new number of visits to the file"""
    try:
        curr_num_visits = int(get_num_of_visits())
    except ValueError:
        curr_num_visits = 0
    with open(os.path.join(os.path.dirname(__file__), 'visits/visits.txt'),
              'w',
              encoding="utf-8") as storage:
        storage.write(str(curr_num_visits + 1))


def get_num_of_visits():
    """get current number of the visits"""
    with open(os.path.join(os.path.dirname(__file__), 'visits/visits.txt'),
              'r',
              encoding="utf-8") as storage:
        return storage.read()
