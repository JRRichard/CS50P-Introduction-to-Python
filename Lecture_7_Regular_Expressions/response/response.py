import validators


def main():
    print(response(input("What's your email address? ")))


def response(s):
    # Read documentation from the validators library
    if validators.email(s.strip()):
        return ("Valid")
    else:
        return ("Invalid")


if __name__ == "__main__":
    main()