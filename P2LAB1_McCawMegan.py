# Megan McCaw
# March 7, 2026
# P2LAB1
# This program will calculate the diameter, circumference, and area of a circle given the radius.

# Import math module to use value of pi
import math

# Ask user for radius of the circle
radius = float(input("What is the radius of the circle? "))
print()

# Calculate the diameter
diameter = 2 * radius

# Return diameter with 1 decimal place
print(f"The diameter of the circle is: {diameter:.1f}\n")

# Calculate the circumference
circumference = 2 * math.pi * radius

# Return circumference with 2 decimal places
print(f"The circumference of the circle is: {circumference:.2f}\n")

# Calculate the area
area = math.pi * radius**2

# Return area with 3 decimal places
print(f"The area of the circle is: {area:.3f}")