from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")

# We disable the animation of the turtle graphics to improve performance and reduce flickering. By setting tracer(0), the screen will only update when we call screen.update(), giving us full control over when the graphics are rendered. This is especially useful in a game like Snake, where we want to update the screen at specific intervals to create smooth animations and improve performance.
screen.tracer(0)

paddle = Turtle(shape="square")
paddle.resizemode("user")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("white")
paddle.penup()
paddle.setposition(350, 0)
paddle.setheading(90)

def up():
    paddle.forward(20)
    screen.update()

def down():
    paddle.backward(20)
    screen.update()

screen.update()

screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)

screen.exitonclick()