from fuel import convert, gauge # Same folder
import pytest # needed to import to get raises module

def main():
    # Call the three test functions
    test_input()
    test_zero_division()
    test_value()


def test_input():
    # Test results from valid inputs
    assert convert('1/5') == 20 and gauge(20) == '20%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'

def test_zero_division():
    # Check for ZeroDivisionError from pytest documentation
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value():
    # Check for non-integer data entry
    with pytest.raises(ValueError):
        convert('bird/flu')



if __name__ == "__main__":
    main()
