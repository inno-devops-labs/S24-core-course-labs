import re


def test_index_returns_time(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Moscow" in response.text
    assert re.search(r"<time>[:\d\s\/,]+</time>", response.text) is not None
