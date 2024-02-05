import datetime
import pytz


def get_formatted_time():
    '''
    Returns formatter MSK time
    '''
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.datetime.now()
    msk_time = now.astimezone(tz)
    return msk_time.strftime("%H:%M:%S %d-%m-%Y")
