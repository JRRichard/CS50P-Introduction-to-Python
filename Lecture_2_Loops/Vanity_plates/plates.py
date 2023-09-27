def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length of string - should be at least 2 but no more than 6
    # Then check first 2 characters
    # Then check for allowed characters
    # Then check for validity of last character if a number is in string
    # Then check if first digit that appears is zero
    return (
        2 <= len(s) <= 6
        and first_two(s)
        and allowed_char(s)
        and last_char(s)
        and first_digit(s)
        and rem_digits(s)
    )
    # return 2<=len(s)<=6 and first_two(s) and rem_digits(s)


def first_two(char):
    # Check first two characters as alpha
    return char[0].isalpha() and char[1].isalpha()


def allowed_char(char):
    # Only alpha numeric characters allowed; no punctuations
    return char.isalnum()


def last_char(char):
    # Check last character to be a digit or only as letter if all others are letters
    last = char[-1]
    return (char[0:-1].isalpha() and last.isalpha()) or last.isdigit()


def first_digit(char):
    # Convert string to list
    letters = list(char)
    # Check for presence of "0" in the string and look for characters before it
    if "0" in letters:
        index_loc = letters.index("0")
        return not (char[0:index_loc].isalpha())
    else:
        return True


def rem_digits(char):
    first_dig = 0
    i = 0
    while i < len(char):
        if char[i].isdigit():
            first_dig = i
            break
        i += 1
    return char[first_dig:].isdigit() or char.isalpha()


if __name__ == "__main__":
    main()
