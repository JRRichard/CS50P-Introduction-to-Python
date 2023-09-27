from bank import value

# Question specifically requests integer value to be returned
def test_hello_first():
    assert value("hello") == 0

def test_h_first_letter():
    assert value("howdy") == 20

def test_non_h_first_letter():
    assert value("pleasure") == 100

def test_number():
    assert value("1") == 100

def test_upper_case():
    assert value("HOWDY") == 20