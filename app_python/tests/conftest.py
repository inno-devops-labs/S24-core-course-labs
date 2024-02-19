import os.path
import sys
from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# To include backend app to path and import it without problems

from api import router as api_router


def start_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_router, prefix="/api")
    return app


@pytest.fixture(scope="function")
def client() -> Generator[TestClient, Any, None]:
    with TestClient(start_app()) as client:
        yield client
