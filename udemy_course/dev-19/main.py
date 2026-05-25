from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# Listening for key presses and binding them to functions
screen.listen()

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

# Binding the space key to the move_forward function
# The key parameter specifies which key to listen for, and the fun parameter specifies the function to call when that key is pressed
# We pass a function as an input to other function
# screen.onkey(key="space", fun=move_forward)

def left():
    timmy.left(10)

def right():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()