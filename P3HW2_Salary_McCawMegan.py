# Megan McCaw
# March 28, 2026
# P3HW2 Salary
# This program calculates the pay of an employee based on their hours worked, hourly wage, and overtime pay.

# Get user input for name, hours worked, and hourly wage
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))


# Calculate overtime hours and pay using an if else statement. Regular hours max out at 40, so regular hour pay can be easily calculated later on.
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_hours = 40
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked

# Store regular hour pay and gross hour pay in variables for use in results.
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Store the - symbol in a variable for reuse
sym = '-'

# Print the employee's name and the header for the salary calculation
print(sym * 40)
print(f"Employee Name: {name}")

# Print a table header for all values, giving each column a width of 15 characters for nice formatting.
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime':<15}{'Overtime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print(sym * 90)

# Print the calculated values with the same formatting as header and two decimal places for the float values. Values with dollar amounts have width of 14 to account for the $.
# Regular hour pay is calculated by multiplying the regular hours by pay rate. Gross pay is the sum of regular hour pay and overtime pay.
print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}{overtime_hours:<15.2f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")

