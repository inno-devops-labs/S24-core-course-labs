import pytest
from app.main import app as main_app


@pytest.fixture()
def app():
    main_app.config.update(
        {
            "TESTING": True,
        }
    )

    yield main_app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
