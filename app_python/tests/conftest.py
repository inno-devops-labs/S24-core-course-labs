import pytest
import datetime


@pytest.fixture
def mock_datetime(monkeypatch, mocked_datetime):
    class MockTime(datetime.datetime):
        @classmethod
        def now(cls):
            return mocked_datetime

    monkeypatch.setattr(datetime, "datetime", MockTime)
