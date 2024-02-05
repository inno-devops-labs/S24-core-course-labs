import pytest
from app.domain.time import TimeManager, TimeManagerConfig


@pytest.fixture(scope="function")
def time_manager_factory():
    async def _factory(data: dict = {}):
        config = TimeManagerConfig(**data)
        return TimeManager(config=config)

    return _factory
