from typing import Optional

import pytest

from app.domain.time import TimeManager, TimeManagerConfig


@pytest.fixture(scope="function")
def time_manager_factory():
    async def _factory(data: Optional[dict] = None):
        if data is None:
            data = {}

        config = TimeManagerConfig(**data)
        return TimeManager(config=config)

    return _factory
