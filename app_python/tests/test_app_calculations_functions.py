from src.app import unify_number


def test_unify_func():
    """
    Tests if app.unify_number() function works correctly.
    """
    assert unify_number(1) == "01"
    assert unify_number(2) == "02"
    assert unify_number(3) == "03"
    assert unify_number(4) == "04"
    assert unify_number(5) == "05"
    assert unify_number(6) == "06"
    assert unify_number(7) == "07"
    assert unify_number(8) == "08"
    assert unify_number(9) == "09"
    assert unify_number(11) == "11"
