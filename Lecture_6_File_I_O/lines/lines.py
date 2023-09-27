import sys

def main():
    print(lines_count())

def lines_count():
    # If no argument provided in command-line, program should exit with xomment
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    # If too many arguments provided in command-line, program should exit with comment
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # If argument in command-line does not nd with ".py", program should exit with comment
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    line=line.lstrip(" ")
                    if not line.startswith(("#", "\n")):
                        count+=1
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            return count




if __name__ == "__main__":
    main()