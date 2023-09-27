import sys
import csv
from tabulate import tabulate

def main():
    print_grid(pizza_table())

def pizza_table():
    # If no argument provided in command-line, program should exit with xomment
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    # If too many arguments provided in command-line, program should exit with comment
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # If argument in command-line does not nd with ".py", program should exit with comment
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]

def print_grid(filename):
    try:
        # Initiate with empty list to add rows (each one a list) from csv file. Returns a list of lists
        menu = []
        with open(filename) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
        # Use tabulate module, modify headers and set format to grid. Read into the documentation
        print (tabulate(menu, headers = "firstrow", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        pass


if __name__ == "__main__":
    main()
