from dataclasses import dataclass
from datetime import datetime


@dataclass
class DateTimeFormatted:
    date: str
    time: str

    @staticmethod
    def from_datetime(date_time: datetime) -> 'DateTimeFormatted':
        return DateTimeFormatted(
            date_time.strftime('%B %d, %Y'), date_time.strftime('%H:%M:%S')
        )
