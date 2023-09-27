def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(long_word):
    # Define vowels in lowercase and get input from user
    vowels = ["a","e","i","o","u"]

    # Start with empty string and then add to desired return
    short_word = ""
    for l in long_word:
        if l.lower() not in vowels:
            short_word+=l
    return(short_word)


if __name__ == "__main__":
    main()
