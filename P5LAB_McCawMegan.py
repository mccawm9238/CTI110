# Megan McCaw
# April 26, 2026
# P5LAB
# This program will simulate a self-checkout machine and return amount of dollars and cents required to make change for a given amount.

import random

# Create a function that takes the amount of change to be given and calculates the number of dollars, quarters, dimes, nickels, and pennies needed to make that change.
def disperse_change(change):

    # Round the change to the nearest penny and convert it to an integer number of total cents.
    change = int(round(change * 100))

    # Store the original change amount in dollars for printing at the end.
    original = change / 100

    print(f"Your change is: ${original:.2f}. You will be given:")

    # Calculate the number of dollars and coins needed to make the change, starting with the largest denomination and working down to the smallest, and subtracting the value of each denomination from the total change as you go.
    dollars = change // 100
    change = change - (dollars * 100)

    quarters = change // 25
    change = change - (quarters * 25)

    dimes = change // 10
    change = change - (dimes * 10)

    nickels = change // 5
    change = change - (nickels * 5)

    pennies = change

    # Round the change to the nearest penny and convert it to an integer number of total cents for accurate printing at the end.
    change = int(round(change * 100))

# Print the number of each denomination, only if the number is greater than 0, and use singular or plural form as needed.
    if dollars > 0:
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")

    if quarters > 0:
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")

    if dimes > 0:
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")

    if nickels > 0:
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")

    if pennies > 0:
        if pennies == 1:
            print(f"{pennies} Penny")
        else:
            print(f"{pennies} Pennies")

# Create a main function that generates a random total owed between $0.01 and $400.00, prompts the user to input the amount of money they want to insert, calculates the change, checks if the user has given enough money, and calls the disperse_change function if they have.
def main ():
    total_owed = round(random.uniform(0.01, 400.00), 2)
    print(f"You owe: ${total_owed:.2f}")

    # Prompt the user to input the amount of money they want to insert and convert it to a float.
    money_given = float(input("How much cash will you put in the self-checkout?: $"))
    # Calculate the change by subtracting the total owed from the money given.
    change = money_given - total_owed

    # Check if the user has given enough money, and if not, print a message and end the program. If they have given enough money, call the disperse_change function to calculate and print the change.
    if change < 0:
        print("You have not given enough money.")
        return
    
    disperse_change(change)


main()
