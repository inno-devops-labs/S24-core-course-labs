"""Test for application"""

from datetime import datetime
from requests import get
from bs4 import BeautifulSoup
import pytz


URL = "http://127.0.0.1:5000"

def test_availability():
    """Test that the site is available"""
    assert get(URL, timeout=1).status_code == 200

def test_time():
    """Test that the site shows correct time"""
    soup = BeautifulSoup(get(URL, timeout=1).text, "html.parser")
    timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    assert soup.p.text == moscow_time
