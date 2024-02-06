import datetime
import pytz
import time

from project import create_app


def test_current_moscow_time(test_client):
    response = test_client.get('/time')
    timezone: datetime.tzinfo = pytz.timezone('Europe/Moscow')
    moscow_time: str = datetime.datetime.now(timezone).strftime("%d %B, %H:%M:%S")
    assert response.status_code == 200
    assert moscow_time in response.text
