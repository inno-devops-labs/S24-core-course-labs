import pytest
from app_python.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture()
def runner():
    return app.test_cli_runner()
