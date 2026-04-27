from calculator import calculate

def test_add():
    assert calculate(2, 3, "add") == 5

def test_subtract():
    assert calculate(5, 2, "subtract") == 3