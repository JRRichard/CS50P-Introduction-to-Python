from um import count

def main():
    test_count()
    test_separate()
    test_punctuation()
    test_case_sensitvity()

def test_count():
    # Test proper counting of length of list
    assert count(r"um um followed by many words um um") == 4


def test_separate():
    # Test that "um" is counted only when separate and not within word
    assert count(r"um um um") == 3
    assert count(r"yummy um in my tummy ummy") == 1


def test_punctuation():
    # Test that "um" is counted even when there is a punctuation mark after it
    assert count(r"um, thanks, um...") == 2
    assert count(r"um?") == 1


def test_case_sensitivity():
    # Test that upper and lowercase are accepted
    assert count(r"Um thanks um") == 2
    assert count(r"UM UM UM") == 3

if __name__ == "__main__":
    main()