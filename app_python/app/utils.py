from datetime import datetime, timezone, timedelta


def get_moscow_time():
    """Return: moscow time in format %Y-%m-%d %H:%M:%S"""
    moscow_tz = timezone(timedelta(hours=3))  # Moscow Time Zone UTC+3
    current_utc_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    moscow_time = current_utc_time.astimezone(moscow_tz)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')
