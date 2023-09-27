from plates import is_valid

def test_length():
    assert is_valid("C") == False
    assert is_valid("CSFE203") == False
    assert is_valid("CS50") == True

def test_first_chars():
    assert is_valid("CS50") == True
    assert is_valid("C500") == False

def test_last_char():
    assert is_valid("CS50P") == False
    assert is_valid("CSFE") == True
    assert is_valid("CS500") == True

def test_zero_location():
    assert is_valid("CS051") == False
    assert is_valid("CS50") == True

def test_digits_after_alpha():
    assert is_valid("CS50P1") == False

def test_punc():
    assert is_valid("CS50!") == False
    