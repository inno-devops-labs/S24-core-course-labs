from app.app_python import app, msc_time


def test_index_status():
    code_response = app.test_client().get('/')
    assert code_response.status_code == 200


def test_msc_time_format():
    response = msc_time()
    assert len(response) == 19
    assert response[4] == '-'
    assert response[7] == '-'
    assert response[10] == ' '
    assert response[13] == ':'
    assert response[16] == ':'


def test_msc_time_response():
    response = msc_time()
    date_str = response.split()[0]
    time_str = response.split()[1]
    assert len(date_str) == 10
    assert len(time_str) == 8
