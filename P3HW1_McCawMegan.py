# Megan McCaw
# March 28, 2026
# P3HW1
# This program takes an inputted grade, determines average, and displays results and letter grade for average.

# Enter grades for six modules and store them in variables, making sure to convert them to floats

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Store the grades in a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Create variables for the lowest grade, highest grade, sum, and average of grades using list methods and calculations

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# Create a variable to store the - symbol for reuse

sym = '-'

# Print the results, formmated nicely with a header and aligned columns, using f strings, width, and decimal rounding.

print(f"{sym * 12}Results{sym*12}")
print(f"{'Lowest grade:':15}{low:15}")
print(f"{'Highest grade:':15}{high:15}")
print(f"{'Sum of grades:':15}{sum:15}")
print(f"{'Average:':15}{avg:15.2f}")
print(f"{sym * 31}")

# Use elif statements to determine letter grade based on average and print the letter grade.

if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





