import pytest

from app import get_current_time


# Test cases for get_current_time function
def test_get_current_time_format():
    # Test if the time returned has the correct format (HH:MM:SS)
    current_time = get_current_time()
    assert isinstance(current_time, str)
    assert len(current_time.split(':')) == 3


if __name__ == "__main__":
    pytest.main()
