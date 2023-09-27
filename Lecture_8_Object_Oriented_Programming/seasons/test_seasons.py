from seasons import check_birthday, diff_calc
    
    
def main():
    test_words_date()
    test_date_format()


def test_words_date():
    assert check_birthday("2023-09-12") == ("2023", "09", "12")
    assert check_birthday("January 1, 1999") == None


def test_date_format():
    assert diff_calc (2023,9,12) == 1440
    assert diff_calc(2023,9,11) == 2880

if __name__ == "__main__":
    main()