from datetime import datetime
import pytz


def get_moscow_date_time():
    utc_now = datetime.utcnow()
    moscow_tz = pytz.timezone('Europe/Moscow')
    return utc_now.replace(tzinfo=pytz.utc).astimezone(moscow_tz)
