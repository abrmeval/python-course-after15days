# Another way to import the turtle module
# import turtle
# timmy = turtle.Turtle()

# Turtle is a built-in module in Python used for drawing and creating graphics.
from turtle import Turtle, Screen

# Another way to import the turtle module (import all)
# from turtle import *

# Aliasing the module
# import turtle as t
# timmy = t.Turtle()

# Importing specific classes from the module
# This needs to be installed via pip
import heroes

print(heroes.gen())


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed(1)

# Draw a square
# for _ in range(4):
# timmy.forward(20)
#     # timmy.forward(100)
#     # timmy.right(90)

# Draw a dashed line
# for _ in range(15):
# xposs = timmy.position()[0]

# timmy.setx(xposs + 20)
# timmy.goto(xposs + 20, 0)
# timmy.setposition(xposs + 20, 0)
# timmy.teleport(xposs + 20)

# Better aproach
#     # timmy.forward(20)
#     # if timmy.isdown():
#     #     timmy.penup()
#     # else:
#     #     timmy.pendown()

# The best aproach
#     timmy.forward(20)
#     timmy.pen(pendown=(not timmy.isdown()))

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# Using a list of shapes with their number of sides and colors
shapes = [
    {"name": "triangle", "sides": 3, "color": "red"},
    {"name": "square", "sides": 4, "color": "blue"},
    {"name": "pentagon", "sides": 5, "color": "green"},
    {"name": "hexagon", "sides": 6, "color": "yellow"},
    {"name": "heptagon", "sides": 7, "color": "orange"},
    {"name": "octagon", "sides": 8, "color": "purple"},
    {"name": "nonagon", "sides": 9, "color": "pink"},
    {"name": "decagon", "sides": 10, "color": "brown"},
]


def draw_shape(sides_number, color_name):
    angle = 360 / sides_number
    length = 100

    for _ in range(0, sides_number):
        timmy.color(color_name)	
        timmy.right(angle)
        timmy.forward(length)

for shape in shapes:
	draw_shape(shape["sides"], shape["color"])


screen = Screen()
screen.exitonclick()
