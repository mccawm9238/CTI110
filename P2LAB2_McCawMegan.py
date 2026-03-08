# Megan McCaw
# March 8, 2026
# P2LAB2
# This program will create a dictionary of cars and their miles per gallon, allow the user to select a car, and calculate how many gallons of gas they will need for a trip based on the distance they will drive.

# Create a dictionary with key:value pairs of car and MPG
cars = {
    'Camaro' : 18.21,
    'Prius' : 52.36,
    'Model S' : 110,
    'Silverado' : 26
}

# Store the keys of the dictionary in a variable
keys = cars.keys()

# Print the keys of the dictionary, each on a new line for readability
print(*keys, sep="\n")

# Ask the user to input a car from the list
user_car = input("Enter a car name exactly as shown above to see its MPG: ")

# Get and print MPG for the user's car
user_mpg = cars[user_car]

print(f"The {user_car} gets {user_mpg} miles per gallon.")

# Ask the user how many miles they will drive the car and store in a variable
user_miles = float(input(f"How many miles will you drive the {user_car}? "))

# Calculate how many gallons of gas the user will need to drive the car for the trip and store in a variable
user_gallons = user_miles / user_mpg

# Print how many gallons of gas the user will need to drive the car for the trip
print(f"You will need {user_gallons:.2f} gallons of gas to drive the {user_car} {user_miles} miles.")