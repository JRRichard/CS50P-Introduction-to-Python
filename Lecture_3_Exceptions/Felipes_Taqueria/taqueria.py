menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    get_total()


def get_total():
    cost = 0
    while True:
        # Get item input from user until user presses control-d
        try:
            item = input("Item: ").lower().title()
        except EOFError:
            print()
            break
        else:
            try:
                price = menu[item]
            except KeyError:
                pass
            else:
                cost = cost + price
                print(f"Total: ${cost:.2f}")
    return None


if __name__ == "__main__":
    main()
