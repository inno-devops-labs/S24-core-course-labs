import pytest
from app import app
from datetime import datetime
import pytz
from flask import template_rendered
from contextlib import contextmanager


# Setup a fixture for the Flask test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Context manager to capture templates used in rendering
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


def test_show_time_status_code(client):
    """Test the show_time endpoint returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200


def test_show_time_content(client):
    """Test the show_time endpoint returns the expected content."""
    with captured_templates(app) as templates:
        response = client.get('/')
        assert len(templates) == 1
        template, context = templates[0]
        assert 'time' in context  # Ensure 'time' is in the context passed to the template
        # Additional checks can be added here to validate the format of 'time' if necessary


def test_home_page_moscow_time(client):
    """Test the home page displays the current Moscow time."""
    result = client.get('/')
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')
    assert moscow_time in result.get_data(as_text=True)
