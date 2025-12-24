# This module demonstrates basic usage of the turtle graphics library
# This library is used to create drawings and shapes using a virtual "turtle" that moves around the screen

# import turtle

# turtle.Turtle()  # Create a new turtle object

# from turtle import Turtle, Screen
# timmy = Turtle()  # Create a new turtle object named timmy
# print(timmy)  # Print the turtle object to the console

# timmy.shape("turtle")  # Change the shape of the turtle to a turtle icon
# timmy.color("blue")  # Set the color of the turtle to blue
# timmy.forward(100)  # Move the turtle forward by 100 units

# my_screen = Screen()  # Create a new screen object named my_screen
# print(my_screen.canvheight)  # Print the height of the canvas to the console
# my_screen.exitonclick()  # Wait for a mouse click on the screen to close it

#PyPi is a repository for python packages
#You can install packages using pip
#Example: pip install prettytable
#Then you can import and use the package in your code
# To install global packages use: pip install --user package_name
# To install local packages use: pip install package_name

# import prettytable

# Create a new virtual environment
# This keeps your project dependencies isolated
#python -m venv .venv

# Activate it
#.venv\Scripts\activate

# Install your package
#pip install prettytable

from prettytable import PrettyTable

table = PrettyTable()  # Create a new PrettyTable object
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # Add a column for Pokemon names
table.add_column("Type", ["Electric", "Water", "Fire"])  # Add a column for Pokemon types   

table.align = "l"  # Align the text to the left

print(table)  # Print the table to the console