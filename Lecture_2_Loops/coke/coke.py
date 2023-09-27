def main():
    # Start with 50 cents and ask user for input. Continue running while amount due is greater than 0
    amount_due = 50
    while amount_due > 0:
        print("Amount Due:", amount_due)
        added_coin = int(input("Insert coin: "))


        if added_coin == 25 or added_coin== 10 or added_coin==5:
            change = change_calculator(amount_due, added_coin) # Use function to calculate value fo change
            if change <= 0:
                print("Change Owed:", change*-1) # Convert change from negative to positive and exit program
                break
            else:
                amount_due = change # Continue program while change > 0
        else:
            amount_due

# Function to calculate change (not necessary but building functions)
def change_calculator(due, coin):
    # Subtract from starting amount and deduct coin added
    result = due - coin
    return result

if __name__ == "__main__":
    main()