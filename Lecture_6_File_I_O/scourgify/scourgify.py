"""In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message."""

import sys
import csv

def main():
    scourgify(comm_line())

def comm_line():
    # If no argument provided in command-line, program should exit with xomment
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # If too many arguments provided in command-line, program should exit with comment
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # If argument in command-line does not nd with ".csv", program should exit with comment
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return (sys.argv[1])


def scourgify(filename):
    try:
        # Initiate with empty list to add rows (each one a list) from csv file. Use DictReader to use first row as heading
        writename = sys.argv[2]
        persons = []
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Separate out the name from the name/house combo and split name by ","
                split_name = row["name"].split(",")
                # Remove extra space found with first name and then add as dictionary in correct order
                persons.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
            #print(persons)

        with open(writename, "w") as file:
            writer = csv.DictWriter (file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for person in persons:
                writer.writerow({"first":person["first"], "last":person["last"], "house":person["house"]})

    except FileNotFoundError:
        sys.exit("Could not read", filename)
    else:
        pass


if __name__ == "__main__":
    main()

