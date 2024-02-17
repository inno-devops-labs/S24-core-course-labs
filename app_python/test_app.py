from app import app
import re

app.config.update({
    "TESTING": True
})

def test_call_time():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_call_time_404():
    client = app.test_client()
    response = client.get('/404')
    assert response.status_code == 404

def test_datetime_range():
    client = app.test_client()
    response = client.get('/')
    assert re.match(r'[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{6}', response.data.decode("utf-8"))