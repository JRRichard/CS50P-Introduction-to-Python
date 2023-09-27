from working import convert
import pytest

def main():
    test_format()
    test_wrong_format()
    test_values_minutes()
    test_values_hours()

def test_format():
    assert convert (r"9 AM to 5 PM") == "09:00 to 17:00"
    assert convert (r"9:30 PM to 5:30 AM") == "21:30 to 05:30"

def test_wrong_format():
    with pytest.raises(ValueError):
        convert(r"9 AM - 5 PM")
        convert(r"9-11 AM")

def test_values_minutes():
    with pytest.raises(ValueError):
        convert(r"9:60 AM to 5:60 PM")

def test_values_hours():
    with pytest.raises(ValueError):
        convert(r"13:00 AM to 10:00 PM")

if __name__ == "__main__":
    main()