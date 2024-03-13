"""
This module contains the model for the current time in Moscow.
"""
import datetime

class TimeModel:
    """
    This class represents the current time in Moscow.
    """
    def __init__(self):
        self.time = datetime.datetime.now(datetime.timezone.utc).astimezone(
            datetime.timezone(datetime.timedelta(hours=3)))