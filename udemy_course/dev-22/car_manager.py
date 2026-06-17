from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POSITION = 300
STARTING_POSITION = (-240, 240)


# THRESHOLD =
class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        pass

    def __new_car(self):
        car = Turtle(shape="square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        ic = random.randint(0, len(COLORS) - 1)
        car.color(COLORS[ic])
        car.setheading(180)
        return car

    def set_car(self):
        car = self.__new_car()
        y_position = random.randint(STARTING_POSITION[0], STARTING_POSITION[1])
        car.penup()
        car.setposition(X_POSITION, y_position)
        self.cars.append(car)

    def move_all(self, player):
        collision_detected = False

        for car in self.cars:
            car.forward(self.move_distance)
            _, car_y = car.position()
            _, player_y = car.position()

            if player.distance(car) < 25 and car_y - player_y < 10:
                collision_detected = True

            if player.distance(car) < 20 and player_y - car_y < 10:
                collision_detected = True

        return collision_detected

    def increase_distance(self):
        self.move_distance += MOVE_INCREMENT

    def destroy_cars(self):
        active_cars = []
        for car in self.cars:
            if car.xcor() <= -320:
                car.clear()
                car.hideturtle()
                continue

            active_cars.append(car)
        self.cars = active_cars

    def detect_collision(self, player):
        pass
