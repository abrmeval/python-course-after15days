from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

# The tracer method is used to control the animation of the turtle graphics.
# By default, turtle graphics are animated, meaning that each movement of the turtle is displayed on the screen.
# However, when you want to create a game or a complex animation, you may want to control when the screen updates to improve performance and reduce flickering.
# The tracer method allows you to do this by setting the number of frames to skip before updating the screen. Setting it to 0 means that the screen will only update when you call the update method, giving you full control over when the graphics are rendered.
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
