import datetime

import pytest

from ..api.time_manager import get_current_time

MOCK_TIME = datetime.datetime(2024, 2, 6, 13, 0)
EXPECTED_TIME = "13:00:00 06-02-2024"


@pytest.fixture
def mock_datetime(monkeypatch):
    class MockTime(datetime.datetime):
        @classmethod
        def now(cls):
            return MOCK_TIME

    monkeypatch.setattr(datetime, "datetime", MockTime)


def test_msktime(mock_datetime):
    assert get_current_time() == EXPECTED_TIME
