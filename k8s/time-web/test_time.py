from time_web import get_time


def test_get_time_format():
    result = get_time()

    assert isinstance(result, str)

    assert "The current time in Moscow is: " in result

    assert len(result) == len("The current time in Moscow is: YYYY-MM-DD HH:MM:SS")
