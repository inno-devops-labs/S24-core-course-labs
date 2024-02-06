def test_get_returns200(client):
    """
    Test the availability of "/" endpoint
    """
    response = client.get("/")
    assert response.status_code == 200


def test_get_time_returns_correct_time(client):
    """
    Test the correctness of time in moscow
    """
    from datetime import datetime
    from pytz import timezone

    response = client.get("/")
    MSK = timezone("Europe/Moscow")
    moscow_time = datetime.now(MSK).strftime("%Y:%m:%d %H:%M:%S %Z %z")
    assert response.json["time"] == moscow_time


def test_get_time_returns_different_time_each_request(client):
    """
    Test chainging time after refreshing
    """
    import time

    response1 = client.get("/")
    time.sleep(1)
    response2 = client.get("/")
    assert response1.json["time"] != response2.json["time"]
