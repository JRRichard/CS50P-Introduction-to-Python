import inflect


def main():
    p = inflect.engine()
    everyone = p.join((adieu()))
    print (f"Adieu, adieu, to {everyone}")



def adieu():    # Similar to preparing the list for grocery
    # Create an empty tuple
    names = ()
    while True:
        try:
            name = input("Name: ")
            #name = input()
            names+= (name,)
        except EOFError:
            return names


if __name__ == "__main__":
    main()
