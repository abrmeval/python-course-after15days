from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# The tracer method is used to control the animation of the turtle graphics.
# By default, turtle graphics are animated, meaning that each movement of the turtle is displayed on the screen.
# However, when you want to create a game or a complex animation, you may want to control when the screen updates to improve performance and reduce flickering.
# The tracer method allows you to do this by setting the number of frames to skip before updating the screen. Setting it to 0 means that the screen will only update when you call the update method, giving you full control over when the graphics are rendered.
screen.tracer(0)

squares = []


def create_square():
    square = Turtle(shape="square")
    square.color("white")
    square.penup()
    squares.append(square)
    return square


def set_position(square, last_x_position=0, last_y_position=0):
    orientation = square.heading()

    if orientation == 0:
        square.goto(last_x_position - 20, last_y_position)
    elif orientation == 90:
        square.goto(last_x_position, last_y_position - 20)
    elif orientation == 180:
        square.goto(last_x_position + 20, last_y_position)
    else:
        square.goto(last_x_position, last_y_position + 20)


def snake_start():
    square = create_square()
    x, y = square.position()

    for i in range(2):
        square = create_square()
        set_position(square, x, y)
        x, y = square.position()


snake_start()

game_is_on = True
while game_is_on:
    size = len(squares)

    #This method is used to update the screen with the latest changes made to the turtle graphics. 
    # When you call screen.update(), it will redraw the entire screen with the current state of all the turtles and their positions.
    # This is especially useful when you have set tracer(0) to control when the screen updates, allowing you to create smoother animations and improve performance by only updating the screen at specific intervals.
    screen.update()
    time.sleep(0.1)

    for x in range(size - 1, 0, -1):
        squares[x].goto(squares[x - 1].position())

    squares[0].forward(20)
    squares[0].left(90)
screen.exitonclick()
