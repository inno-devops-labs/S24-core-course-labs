"""
Web app unit tests conftest
"""

from app.app import wsgi_app
import pytest


@pytest.fixture()
def flask_app():
    """
    Pytest app fixture
    """
    f_app = wsgi_app
    f_app.config.update({"TESTING": True})
    yield f_app


@pytest.fixture()
def client(flask_app):
    """
    Pytest client fixture
    """
    return flask_app.test_client()


@pytest.fixture()
def runner(flask_app):
    """
    Pytest runner fixture
    """
    return flask_app.test_cli_runner()
