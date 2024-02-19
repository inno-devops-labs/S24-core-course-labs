import pytest
from webtest import TestApp
from datetime import datetime, timezone
from app import app as myapp


@pytest.fixture
def app():
    return TestApp(myapp)


@pytest.fixture
def mock_datetime(monkeypatch):
    # A function to replace datetime.datetime.now
    class MockDateTime:
        @classmethod
        def now(cls, tz=None):
            return datetime(2023, 1, 1, 12, 0, 0, tzinfo=timezone.utc)

    monkeypatch.setattr("app.datetime.datetime", MockDateTime)
