import pytest
from dateutil import parser
from fastapi.testclient import TestClient

from app.main import app
from app.services.time import get_time_in_msk

const_time = "2024-02-19T22:19:11.112401+03:00"


async def mock_get_time_in_msk():
    return parser.parse(const_time)


app.dependency_overrides[get_time_in_msk] = mock_get_time_in_msk

client = TestClient(app)


@pytest.mark.asyncio
async def test_override_in_items():
    print(await mock_get_time_in_msk())
    assert await mock_get_time_in_msk()
    response = client.get("/time/msk/")
    assert response.json() == {
        "current_time": const_time
    }
