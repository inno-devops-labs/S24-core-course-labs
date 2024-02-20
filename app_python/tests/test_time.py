import datetime
import pytz

import pytest

from ..api.time_manager import get_current_time

MOCK_TIME = datetime.datetime(
    2024, 2, 6, 13, 0, tzinfo=pytz.timezone("Europe/Moscow"))
MOCK_DATE_NY = datetime.datetime(
    2024, 2, 6, 5, 4, tzinfo=pytz.timezone("America/New_York")
)

EXPECTED_TIME = "13:00:00 06-02-2024"


@pytest.mark.parametrize("mocked_datetime", [MOCK_DATE_NY, MOCK_TIME])
def test_msktime(mock_datetime):
    assert get_current_time() == EXPECTED_TIME
