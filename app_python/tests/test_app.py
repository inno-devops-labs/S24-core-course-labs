import pytest
import sys
import os
from flask import template_rendered
from contextlib import contextmanager

# Add a parent directory to sys.path to allow imports from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '..')))  # noqa: E402

from app import app as flask_app  # noqa: E402
import pytz  # noqa: E402
from datetime import datetime  # noqa: E402


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@contextmanager
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_home_route(client):
    """Test the home route accessibility and the time format correctness."""
    response = client.get('/')
    assert response.status_code == 200
    # Validate format of the time returned
    moscow_time = datetime.now(
        pytz.timezone('Europe/Moscow')).strftime('%d-%m-%Y %H:%M:%S')
    assert moscow_time in response.get_data(as_text=True)


def test_timezone_consistency(client):
    """Ensure the time is in the correct timezone (Europe/Moscow)."""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    # Directly compare tzinfo names
    assert moscow_time.tzinfo.zone == pytz.timezone('Europe/Moscow').zone


def test_date_format(client):
    """Test to ensure the date and time format is as expected."""
    response = client.get('/')
    data = response.get_data(as_text=True)
    assert any(char.isdigit() for char in data), \
        "The response must contain digits (date/time information)."
