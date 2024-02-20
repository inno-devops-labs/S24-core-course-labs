from datetime import datetime, timedelta

import ntplib
import pytest
import pytz
from fastapi.testclient import TestClient
from httpx import Response
from starlette import status

from app_python.main import app

client = TestClient(app)


def string_to_datetime(dt: str) -> datetime:
    return datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%f%z')


def get_utc_offset(dt: datetime) -> timedelta:
    return dt.tzinfo.utcoffset(datetime.now())


class TestGlobalMoscowTime:
    """A class to test the logic of root endpoint."""

    @pytest.fixture
    def response(self) -> Response:
        return client.get("/")

    def test_global_moscow_time_status(self, response):
        """
        Testing that the response has valid status code.
        """
        assert response.status_code == status.HTTP_200_OK, "Wrong response status code!"

    def test_global_moscow_time_time_format(self, response):
        response_json = response.json()
        try:
            datetime.strptime(response_json["moscow_time"], '%Y-%m-%dT%H:%M:%S.%f%z')
        except ValueError:
            raise pytest.fail("Wrong datetime format!")

    def test_global_moscow_time_timezone(self, response):
        """
        Testing that the api datetime is in Moscow timezone.
        """
        response_json = response.json()
        api_moscow_datetime = string_to_datetime(response_json["moscow_time"])
        assert get_utc_offset(api_moscow_datetime) == \
               get_utc_offset(datetime.now(pytz.timezone("Europe/Moscow"))), "Wrong response timezone!"

    def test_global_moscow_time_time(self, response):
        """
        Testing the correspondence of the api time to the NTP server Moscow time.
        """
        response_json = response.json()
        api_moscow_time = string_to_datetime(response_json["moscow_time"]).timestamp()
        current_moscow_time = float(ntplib.NTPClient().request("pool.ntp.org").tx_time)
        assert api_moscow_time == pytest.approx(current_moscow_time, 1.0e-3), \
            "Wrong response time!"
