from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)
