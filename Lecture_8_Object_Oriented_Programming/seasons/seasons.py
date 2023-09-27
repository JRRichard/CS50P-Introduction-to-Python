from datetime import date
import inflect
import re
import sys


def main():
    inputted_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(inputted_date)
    except:
        sys.exit("Invalid Date") # Exit if format is incorrect
    print(convert_to_words(diff_calc(year, month, day)).capitalize() + " minutes")


def diff_calc(year, month, day):
    try:
        birth_date = date(int(year), int(month), int(day))
    except:
        sys.exit("Invalid Date") # Exit if date is not within correct range
    today_date = date.today()
    days_diff = today_date - birth_date # produces a timedelta object
    minutes_diff = days_diff.days * 24 * 60
    return minutes_diff
    


def check_birthday(inputted_date):
    inputted_date = inputted_date.strip()
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", inputted_date): # Get the desired format of date
        year, month, day = inputted_date.split("-")
        return year, month, day
    

def convert_to_words(n):
    p = inflect.engine()
    words = p.number_to_words(n, andword="")
    return words

if __name__ == "__main__":
    main()
