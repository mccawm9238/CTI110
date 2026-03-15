# Megan McCaw
# March 14, 2026
# P2HW1
# This program will take the user's budget and expenses for a trip and calculate the remaining balance in a nice format.
# Pseudocode:
# 1. Ask for the user's budget and store it in a variable.
# 2. Ask for the user's travel destination and store it in a variable.
# 3. Ask for the user's estimated expenses for gas, accommodation, and food, and store them in variables, making sure to convert them to floats.
# 4. Calculate the total expenses by adding gas, accommodation, and food and store it in expenses variable.
# 5. Calculate the remaining balance by subtracting expenses from budget and store it in remaining_balance variable.
# 6. Print the travel destination, initial budget, and individual expenses.
# 7. Print the remaining balance after expenses.


budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you spend on accommodation? "))
food = float(input("Last, how much do you need for food? "))
expenses = gas + accommodation + food
remaining_balance = budget - expenses

# Store the symbol for the header styling for reuse
sym = '-'

# Give all the strings the same width for alignment and print the header and results with two decimal places.
print(f"{sym * 12} Travel Expenses {sym * 12}")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${accommodation:.2f}")
print(f"{'Food:':20}${food:.2f}")
print(f"{sym * 41}")

print(f"{'Remaining Balance:':20}${remaining_balance:.2f}")