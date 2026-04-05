# Megan McCaw
# April 5, 2026
# P4LAB1
# This program will use turtle and loops to draw a square and triangle

# Import turtle library

import turtle

# Create window and change background color
win = turtle.Screen()
win.bgcolor("lightblue")

# Create turtle and change shape, color, and pen size
t = turtle.Turtle()
t.shape("turtle")
t.color("hotpink")
t.pensize(3)


# Create while loop to draw a line for all 3 sides of the triangle
t.fillcolor("lavender")
t.begin_fill()

i = 0

while i < 3:
    t.forward(100)
    t.left(120)

    i = i + 1

t.end_fill()

# Move turtle to location to draw square
t.right(90)
t.forward(100)
t.left(90)

# Create for loop to draw a line for all 4 sides of the square
t.fillcolor("yellow")
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.left(90)

t.end_fill()


# Just for fun, added a grass line :)
t.penup()
t.forward(450)
t.left(180)
t.color("green")
t.pendown()
t.forward(800)


# Exit window on click
turtle.exitonclick()