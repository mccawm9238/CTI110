# Megan McCaw
# March 1, 2026
# P1HW1
# This program will perform will take integers inputted by the user and print the results of each calculation

print('----Calculating Exponents----')

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
power = base**exponent

print(base, 'raised to the power of', exponent, 'is', power, '!!')

print('----Addition and Subtraction----')

starting = int(input("Enter a starting integer: "))
add = int(input("Enter an integer to add: "))
subtract = int(input("Enter an integer to subtract: "))
result = starting + add - subtract

print(starting, '+', add, '-', subtract, 'is equal to', result)