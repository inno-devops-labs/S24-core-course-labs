import pytz
from datetime import datetime


class TimeService:
    def __init__(self, timezone_str='Europe/Moscow'):
        self._timezone_str = timezone_str

    def get_current_datetime(self) -> datetime:
        timezone = pytz.timezone(self._timezone_str)
        current_time = datetime.now(timezone)
        return current_time

    def get_current_time_str(self, date_format='%Y-%m-%d %H:%M:%S') -> str:
        current_time = self.get_current_datetime().strftime(date_format)
        return current_time
