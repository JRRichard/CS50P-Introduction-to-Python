def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Remove dollar sign prefix and then convert to float
    result = float(d.removeprefix("$"))
    return result


def percent_to_float(p):
    # Remove percentage sign suffix, convert to float and then divide by 100
    result = float(p.removesuffix("%"))/100
    return result


main()
