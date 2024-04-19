from pathlib import Path
from typing import Optional

import pytest

from app.domain.visits import VisitsFileStorage, VisitsFileStorageConfig


@pytest.fixture(scope="function")
def visits_storage_factory():
    async def _factory(data: Optional[dict] = None):
        if data is None:
            data = {}

        config = VisitsFileStorageConfig(**data, file_path=Path("visits"))
        return VisitsFileStorage(config=config)

    return _factory
