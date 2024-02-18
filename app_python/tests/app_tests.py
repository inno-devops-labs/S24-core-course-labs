"""Test for application"""

from datetime import datetime
from bs4 import BeautifulSoup
import pytz

from app_python.app import current_moscow_time
from app_python.app import app


def test_current_moscow_time():
    """Unit test for current_moscow_time function"""
    result_time = datetime.strptime(current_moscow_time(), '%Y-%m-%d %H:%M:%S')

    timezone = pytz.timezone('Europe/Moscow')
    expected_time = datetime.now(timezone)

    result_time = result_time.replace(second=0, microsecond=0)
    expected_time = expected_time.replace(second=0, microsecond=0)

    assert str(result_time) == str(expected_time.strftime('%Y-%m-%d %H:%M:%S'))


def test_site_time():
    """Test that the site shows correct time"""
    soup = BeautifulSoup(app.test_client().get("/").text, "html.parser")
    timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    assert soup.p.text == moscow_time
