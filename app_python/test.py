import requests
from bs4 import BeautifulSoup
import pytz
from datetime import datetime

URL = "http://127.0.0.1:8000/"

def test_site_availability():
    response = requests.get(URL, timeout=1)
    assert response.status_code == 200

def test_site_time_display():
    response = requests.get(URL, timeout=1)
    soup = BeautifulSoup(response.text, "html.parser")
    moscow_timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_timezone).strftime('%d-%m-%Y %H:%M:%S')
    div = soup.findAll("div", {"id": "time-display"})[0]
    assert div.text == current_time

# if __name__ == "__main__":
#     test_site_availability()
#     test_site_time_display()
