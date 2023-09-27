import sys
from PIL import Image, ImageOps


def main():
    shirt(comm_line())


def comm_line():
    ending = (".jpg", ".jpeg", ".png")
    # If no argument provided in command-line, program should exit with xomment
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # If too many arguments provided in command-line, program should exit with comment
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # If argument in command-line does not nd with ".csv", program should exit with comment
    elif not sys.argv[1].lower().endswith(ending) or not sys.argv[2].lower().endswith(ending):
        sys.exit("Invalid output")
    elif sys.argv[1].lower().split(".")[1] != sys.argv[2].lower().split(".")[1]:
        sys.exit("Input and output have different extensions")
    else:
        return (sys.argv[1])


def shirt(filename):
    try:
        shirt = Image.open("shirt.png")
        #print(shirt.size) # Follow hint in exercise

        with Image.open(filename) as person:
            resized_person = ImageOps.fit(person, shirt.size)       # Read the documentation

        resized_person.paste(shirt, shirt)          # Read the documentation and follow hint in exercise

        return (resized_person.save(sys.argv[2]))     # Read the documentation

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
