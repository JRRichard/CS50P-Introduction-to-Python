from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(5)
    

if __name__ == "__main__":
    main()