import pytest

def add_numbers(a, b):
    return a + b

def test_addition():
    assert add_numbers(10, 15) == 25
    assert add_numbers(-5, 5) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(3.5, 2.5) == 6.0
    assert add_numbers(-3, -7) == -10

if __name__ == "__main__":
    pytest.main()
