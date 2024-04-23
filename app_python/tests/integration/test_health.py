from tests.integration.config import client


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.text == '"OK"'
