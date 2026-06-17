import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
traffic_light = ["GREEN", "YELLOW", "RED"]

screen.listen()
screen.onkey(key="Up", fun=turtle.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # this function allow to set the probability of selection for every item in a collection
    lights = random.choices(traffic_light, weights=[0.15, 0.35, 0.50], k=1)
    
    # Probability to add a new car
    if lights[0] == "GREEN":
        car_manager.set_car()

    # Collision with car
    collision_detected = car_manager.move_all(turtle)

    if collision_detected:
        game_is_on = False
        scoreboard.game_over()

    if turtle.is_at_finish_line():
        turtle.set_starting_position()
        car_manager.increase_distance()
        scoreboard.update_score()

    car_manager.destroy_cars()
screen.exitonclick()
