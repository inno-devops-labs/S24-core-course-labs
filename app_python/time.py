from datetime import datetime
import pytz


def getMoscowTime(timezone='Europe/Moscow'):
    moscow_tz = pytz.timezone(timezone)
    return datetime.now(moscow_tz).strftime('%H:%M:%S')
