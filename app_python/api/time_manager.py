import datetime

from pytz import timezone

TIME_FORMAT = "%H:%M:%S %d-%m-%Y"


def get_current_time():
    time_zone = timezone("Europe/Moscow")
    current_msk_time = datetime.datetime.now().astimezone(time_zone)
    return current_msk_time.strftime(TIME_FORMAT)
