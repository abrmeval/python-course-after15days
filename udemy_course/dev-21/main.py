from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")

# We disable the animation of the turtle graphics to improve performance and reduce flickering. By setting tracer(0), the screen will only update when we call screen.update(), giving us full control over when the graphics are rendered. This is especially useful in a game like Snake, where we want to update the screen at specific intervals to create smooth animations and improve performance.
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    x, y = ball.position()

    # Collision with the wall  up and down
    if y > 280 or y < -280:
        ball.bounce_y()
        continue

    # Collision with right paddle
    if x > 330 and ball.distance(r_paddle) <= 50:
        ball.bounce_x()
        continue
    # Collision with left paddle
    if x < -330 and ball.distance(l_paddle) <= 50:
        ball.bounce_x()
        continue

    # Right paddle misses the ball
    if x > 380:
        # game_is_on = False
        ball.reset_position()
        scoreboard.l_point()
        continue

    # Left paddle misses the ball
    if x < -380:
        ball.reset_position()
        scoreboard.r_point()

    print(ball.distance(r_paddle))

screen.exitonclick()
