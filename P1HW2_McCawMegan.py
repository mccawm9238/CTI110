# Megan McCaw
# March 1, 2026
# P1HW2
# This program will take the user's budget and expenses for a trip and calculate the remaining balance.
# Pseudocode:
# 1. Ask for the user's budget and store it in a variable.
# 2. Ask for the user's travel destination and store it in a variable.
# 3. Ask for the user's estimated expenses for gas, accommodation, and food, and store them in variables, making sure to convert them to integers.
# 4. Calculate the total expenses by adding gas, accommodation, and food and store it in expenses variable.
# 5. Calculate the remaining balance by subtracting expenses from budget and store it in remaining_balance variable.
# 6. Print the travel destination, initial budget, and individual expenses.
# 7. Print the remaining balance after expenses.


budget = int(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you spend on accommodation? "))
food = int(input("Last, how much do you need for food? "))
expenses = gas + accommodation + food
remaining_balance = budget - expenses

print('------------Travel Expenses------------')
print('Location: ' + destination)
print('Initial Budget:', budget)

print('Fuel:', gas)
print('Accommodation:', accommodation)
print('Food:', food)

print('Remaining Balance:', remaining_balance)