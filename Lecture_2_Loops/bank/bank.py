def main():
    # Get user input for greeting
    first_words = input("Greeting: ")
    print(f"${value(first_words)}")


def value(greeting):
    # Strip whitespaces and check if first letters are "hello"
    if greeting.lower()[:5]=="hello":
        return 0
    # Determine if first word starts with "h" and return integer
    elif greeting.lower()[0]== "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
