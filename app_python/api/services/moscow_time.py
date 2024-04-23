from datetime import datetime
import pytz


def get_current_moscow_time():
    msk_timezone = pytz.timezone("Europe/Moscow")
    cur_time = datetime.now(msk_timezone)
    return cur_time


def get_current_moscow_time_str():
    return get_current_moscow_time().strftime("%d/%m/%Y, %H:%M:%S")
