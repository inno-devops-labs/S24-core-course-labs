from datetime import datetime

import pytz


async def get_time_in_msk():
    return datetime.now(tz=pytz.timezone("Europe/Moscow"))
