def main():
    grocery_list()


# Create empty dictionary to add grocery list items as keys and number of items as values
grocery = {}

def grocery_list():
    while True:
    # Get grocery list item input from user
        try:
            item = input().upper()
            # Check for existence of item; add 1 if already exist or create with 1 if it does not exist
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            print()
            break
        else:
            pass
    for item in sorted(grocery):
        print (grocery[item], item)


if __name__ == "__main__":
    main()
