from fastapi.testclient import TestClient

from src.app import app, create_visit

create_visit()
client = TestClient(app)
