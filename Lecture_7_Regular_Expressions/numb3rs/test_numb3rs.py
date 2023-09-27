from numb3rs import validate

def main():
    # Call two test functions to validate format and numbers being within range
    test_format()
    test_input_range()

def test_format():
    assert validate (r"255.255.255.255") == True
    assert validate (r"cat") == False
    assert validate (r"1.1.1") == False
    assert validate (r"cat.dog.bird.fish") == False
    assert validate (r"1.2") == False
    assert validate (r"255") == False

def test_input_range():
    assert validate (r"1.1.1.1") == True
    assert validate (r"512.1.1.1") == False
    assert validate (r"1.512.1.1") == False
    assert validate (r"1.1.1000.1") == False
    assert validate (r"1.1.1.256") == False

if __name__ == "__main__":
    main()