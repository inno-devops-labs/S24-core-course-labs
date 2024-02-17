import asyncio

import pytest
from fastapi.testclient import TestClient

from app.api import app, di


@pytest.fixture()
async def app_mock(time_manager_factory) -> TestClient:
    client = TestClient(app)
    app.dependency_overrides[di.time_manager] = time_manager_factory
    return client


@pytest.mark.asyncio
async def test_current_time_moscow_update(app_mock):
    app = await app_mock

    resp1 = app.get("/")
    assert resp1.status_code == 200

    data = resp1.text

    await asyncio.sleep(1)

    resp2 = app.get("/")
    assert resp2.status_code == 200
    assert resp2.text != data
