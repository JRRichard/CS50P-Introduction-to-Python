def main():
    # Build function to get user input and print result
    percent = get_percent()
    print(percent)


def get_percent():
    while True:
        # Check user input in the correct format by splitting on "/" character
        fraction = input("Fraction: ")
        fraction = fraction.split("/")
        # Check that both characters are integers
        # Get result
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            result = x / y * 100
        except (ValueError, ZeroDivisionError):
            pass
        # Determine what to return. If less than 1%, return E; if more than 99% but less than or equal to 100%, return F;
        # if more than 100%, reprompt;
        # otherwise return result with no decimals
        else:
            if result <= 1:
                return "E"
            elif 99 <= result <= 100:
                return "F"
            elif result > 100:
                pass
            else:
                return f"{result:.0f}%"


if __name__ == "__main__":
    main()
