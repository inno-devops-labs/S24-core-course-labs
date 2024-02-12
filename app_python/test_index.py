import time
import requests

INDEX_URL = "http://127.0.0.1:8000"

def test_status():
    resp = requests.get(INDEX_URL)
    assert resp.status_code == 200


def test_text_changes():
    resp = requests.get(INDEX_URL)
    text1 = resp.text

    time.sleep(3)

    resp = requests.get(INDEX_URL)
    text2 = resp.text

    assert text1 != text2
