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
print (heroes.gen())


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()