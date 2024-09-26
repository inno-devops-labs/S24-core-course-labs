import time
import datetime
import pytz

from fastapi.testclient import TestClient
from bs4 import BeautifulSoup

from .main import app

INDEX_URL = "http://127.0.0.1:8000"

client = TestClient(app)


def test_status():
    resp = client.get(INDEX_URL)
    assert resp.status_code == 200


def test_text_changes():
    resp = client.get(INDEX_URL)
    text1 = resp.text

    time.sleep(3)

    resp = client.get(INDEX_URL)
    text2 = resp.text

    assert text1 != text2


def test_time_equality():
    resp = client.get(INDEX_URL)
    text = resp.text

    soup = BeautifulSoup(text, 'html.parser')
    time_element = soup.find('div', class_='time')

    time_text = time_element.text.strip()
    time_parsed = datetime.datetime.strptime(time_text, '%Y-%m-%d %H:%M:%S')

    time_real = (datetime.datetime.now(pytz.timezone("Europe/Moscow"))
                 .replace(microsecond=0)
                 .replace(tzinfo=None))

    assert time_parsed == time_real
