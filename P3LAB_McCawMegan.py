# Megan McCaw
# March 22, 2026
# P3LAB
# This program will take a user inputted amount of money and calculate how many of each bill and coin make up that amount.

# Ask the user to input an amount of money and convert it to a float.
money = float(input("Enter an amount of money: $"))

# Round the money to the nearest penny and convert it to an integer number of total cents.
money = int(round(money * 100))

# Calculate the number of dollars by dividing the total cents by 100 and then subtracting the value of the dollars from the total cents to move on to the next denomination.
dollars = money // 100
money = money - (dollars * 100)

# Calculate the number of quarters by dividing the remaining cents by 25 and then subtracting the value of the quarters from the total cents to move on to the next denomination.
quarters = money // 25
money = money - (quarters * 25)

# Calaculate the number of dimes by dividing the remaining cents by 10 and then subtracting the value of the dimes from the total cents to move on to the next denomination.
dimes = money // 10
money = money - (dimes * 10)

# Calculate the number of nickels by dividing the remaining cents by 5 and then subtracting the value of the nickels from the total cents to move on to the next denomination.
nickels = money // 5
money = money - (nickels * 5)

# Calculate the number of pennies by taking the remaining cents as the number of pennies.
pennies = money

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

