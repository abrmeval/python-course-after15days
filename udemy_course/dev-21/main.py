from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")

# We disable the animation of the turtle graphics to improve performance and reduce flickering. By setting tracer(0), the screen will only update when we call screen.update(), giving us full control over when the graphics are rendered. This is especially useful in a game like Snake, where we want to update the screen at specific intervals to create smooth animations and improve performance.
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on=True

while game_is_on:
    screen.update()

screen.exitonclick()