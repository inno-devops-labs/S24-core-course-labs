from app_python.main import get_moscow_time


def test_get_moscow_time_formats_correctly():
    time_string = get_moscow_time()
    assert len(time_string) == 8
    assert time_string[2] == ":"
    assert time_string[5] == ":"
    assert time_string[:2].isnumeric()
    assert time_string[3:5].isnumeric()
    assert time_string[6:].isnumeric()
