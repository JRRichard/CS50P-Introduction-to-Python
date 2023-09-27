"""
In a file called game.py, implement a program that:

    Prompts the user for a level,

. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.

    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.

"""

import random


def main():
    guess_num()


def guess_num():
    while True:
        # Check for value error or if entered value for limit is less than 1
        try:
            lim = int(input("Level: "))
            if lim < 1:
                continue
        except ValueError:
            continue
        # Set random number using random function
        num = random.randint(1, lim)

        while True:
            # Check for ValueError of if enter guess for number is less than 1
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    continue
                if guess == num:
                    print ("Just right!")
                    break
                elif guess > num:
                    print ("Too large!")
                    pass
                elif guess < num:
                    print ("Too small!")
                    pass
            except ValueError:
                pass
        return None


if __name__ == "__main__":
    main()
