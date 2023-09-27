"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve.
For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE.
And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:
    Prompts the user for a level,n. If the user does not input 1, 2, or 3, the program should prompt again.
    Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
    Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
    The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3
"""

import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1,4):
                raise ValueError        # raise value error to allow loop to restart at exception
        except ValueError:
            continue
        else:
            return level


def generate_integer(level):
    wrong = 0           # initiate a counter for incorrect after 3 tries
    count = 0           # Initiate a counter to track number of questions asked
    while count < 10:
        if level == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
        # Initiate a counter for incorrect tries and stay in loop unitl 3 tries and then increase wrong count by 1, provide answer and restart at same level
        error_count = 0
        while error_count < 3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if ans != x + y:
                    raise ValueError
                else:
                    break       # exit loop looking for errors and go to outside of "while" loop to count +=1
            except ValueError:
                error_count+=1
                print ("EEE")
                continue
        else:
            print (f"{x} + {y} = ", x+y)
            wrong += 1
            pass
        count+=1
    print ("Score: ", count-wrong)          # Print final score after count == 10 and subtract answers that were not solved


if __name__ == "__main__":
    main()
