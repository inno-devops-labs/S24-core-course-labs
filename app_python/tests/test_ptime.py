from ptime.utils.utils import get_formatted_time
import pytz
import pytest
import datetime

MOCK_DATE1 = datetime.datetime(
    2024, 1, 2, 6, 59, 0, tzinfo=pytz.timezone("Europe/London")
) 
MOCK_DATE2 = datetime.datetime(2024, 1, 2, 10, 0, tzinfo=pytz.timezone("Europe/Moscow"))


@pytest.fixture
def mock_datetime(monkeypatch, date):
    class MockedDate:
        @classmethod
        def now(cls, *_args, **_kwargs):
            return date

    monkeypatch.setattr(datetime, "datetime", MockedDate)


@pytest.mark.parametrize("date", [MOCK_DATE1, MOCK_DATE2])
def test_get_formatted_time_london(mock_datetime):
    assert get_formatted_time() == "10:00:00 02-01-2024"
