import os
import pytest

from app import app


@pytest.fixture()
def test_client():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'

    # Creating a test client with testing configuration
    with app.test_client() as test_client:
        with app.app_context():
            # Yielding test client for it to be used among other tests
            yield test_client
