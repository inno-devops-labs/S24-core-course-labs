from fastapi.testclient import TestClient
from datetime import datetime, timezone, timedelta
from pyquery import PyQuery

from main import app

client = TestClient(app)


def test_read_root():
    d = datetime.now(timezone(timedelta(hours=3))).strftime("%H:%M:%S")
    res = client.get("/")
    assert res.status_code == 200

    pq = PyQuery(res.text)
    d1 = datetime.strptime(str(pq("p#time").text()), "%H:%M:%S")
    d2 = datetime.strptime(d, "%H:%M:%S")
    assert abs((d1 - d2).total_seconds()) < 5
