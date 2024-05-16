import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.filterwarnings("ignore:.*url_parse.*:DeprecationWarning")
@pytest.mark.filterwarnings("ignore:.*URL.*:DeprecationWarning")
def test_index(client):
    response = client.get('/')
    assert response.status_code ==   200
    assert b'Current Time in Moscow' in response.data

