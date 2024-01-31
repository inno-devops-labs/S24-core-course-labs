from datetime import datetime

import pytz


def get_formatted_moscow_time() -> str:
    tz = pytz.timezone("Europe/Moscow")
    moscow = datetime.now(tz)
    return moscow.strftime("%d/%m/%Y, %H:%M:%S")
