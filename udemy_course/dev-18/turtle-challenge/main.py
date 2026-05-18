# Another way to import the turtle module
# import turtle
# timmy = turtle.Turtle()

# Turtle is a built-in module in Python used for drawing and creating graphics.
from turtle import Turtle, Screen, colormode
import random

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

# Challenge 3
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# Using a list of shapes with their number of sides and colors
# shapes = [
#     {"name": "triangle", "sides": 3, "color": "red"},
#     {"name": "square", "sides": 4, "color": "blue"},
#     {"name": "pentagon", "sides": 5, "color": "green"},
#     {"name": "hexagon", "sides": 6, "color": "yellow"},
#     {"name": "heptagon", "sides": 7, "color": "orange"},
#     {"name": "octagon", "sides": 8, "color": "purple"},
#     {"name": "nonagon", "sides": 9, "color": "pink"},
#     {"name": "decagon", "sides": 10, "color": "brown"},
# ]


# def draw_shape(sides_number, color_name):
#     angle = 360 / sides_number
#     length = 100

#     for _ in range(0, sides_number):
#         timmy.color(color_name)
#         timmy.right(angle)
#         timmy.forward(length)


# for shape in shapes:
#     draw_shape(shape["sides"], shape["color"])


# Challenge 4
timmy.pensize(8)
timmy.speed(5)


def get_random_angle():
    index = random.randint(0, 3)
    return [0, 90, 180, 270][index]


def get_random_color():
    index = random.randint(0, 7)
    return [
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "pink",
        "brown",
    ][index]


# while range(0, 250):
#     timmy.color(get_random_color())
#     timmy.setheading(get_random_angle())
#     timmy.forward(30)


# Python Tuples
# A tuple is a collection which is ordered and *unchangeable*. In Python tuples are written with round brackets.
# my_tuple = (1, 2, 3)
# print(my_tuple[0])  # Output: 1

# Convert a tuple to a list
# my_list = list(my_tuple)

# Set the color mode to RGB (Red, Green, Blue)
colormode(255)

def random_rgb_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# while range(0, 250):
#     timmy.color(random_rgb_color())
#     timmy.setheading(get_random_angle())
#     timmy.forward(30)


# Challenge 5
timmy.pensize(1)
# timmy.shape("circle")
# timmy.shapesize(stretch_wid=0.5, stretch_len=0.5)
timmy.speed(0)

# for x in range(0, 360, 5):
#     timmy.color(random_rgb_color())
#     timmy.circle(100)
#     # timmy.tilt(30)
#     timmy.setheading(x)
#     timmy.tiltangle()
#     # timmy.forward(30)
#     print(timmy.heading())

def draw_spirograph(size_of_gap):
    for x in range(int(360 / size_of_gap)):
        timmy.color(random_rgb_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

def draw_spirograph2(size_of_gap):
    for s in range(0, 360, size_of_gap):
        timmy.color(random_rgb_color())
        timmy.circle(100)
        timmy.setheading(s)

screen = Screen()

draw_spirograph(5)
timmy.clear()
draw_spirograph2(5)

screen.exitonclick()