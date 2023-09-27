import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # use findall to return a list
    list_of_um = re.findall(r"\bum\b",s, re.IGNORECASE) # look for um at start f word and at end of word with \b
    return len(list_of_um)


if __name__ == "__main__":
    main()
