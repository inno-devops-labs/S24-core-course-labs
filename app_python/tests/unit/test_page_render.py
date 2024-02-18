def test_home_page_render(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert 'Current Moscow Time' in response.text
    assert '<div class="time">' in response.text
