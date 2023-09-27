def main():
    # Build function to get user input and print result
    fraction = input("Fraction: ")
    percent_converted = convert(fraction)
    answer = gauge(percent_converted)
    print(answer)


def convert(user_input):
    while True:
    # Check user input in the correct format by splitting on "/" character
        x,y = user_input.split("/")
        try:
            x = int(x)
            y = int(y)
            converted = x/y*100
            # Check for validity of response i.e. numbers given are within 0 and 100
            if 0 <= converted <= 100:
                return converted
            else:
                user_input = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise


def gauge(result):
        if result <=1:
            return ("E")
        elif 99<= result <= 100:
            return ("F")
        else:
            return (f"{result:.0f}%")

if __name__ == "__main__":
    main()

