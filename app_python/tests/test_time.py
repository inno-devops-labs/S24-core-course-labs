def test_current_time_in_moscow_with_mock(app, mock_datetime):
    expected_time = "2023-01-01 15:00:00"
    response = app.get("/")
    assert response.status_code == 200
    assert expected_time in response.text
