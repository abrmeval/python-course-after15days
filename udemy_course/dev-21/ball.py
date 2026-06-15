from turtle import Turtle

MOVE_DISTANCE = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.move_distance_x = MOVE_DISTANCE * 1.35
        self.move_distance_y = MOVE_DISTANCE
        self.move_speed = 0.1

    def move(self):
        x, y = self.position()
        self.goto(x + self.move_distance_x, y + self.move_distance_y)

    def bounce_y(self):
        self.move_distance_y *= -1

    def bounce_x(self):
        self.move_distance_x *= -1
        self._increase_speed()

    def reset_position(self):
        self.move_speed = 0.1
        self.home()
        self.bounce_x()

    def _increase_speed(self):
        self.move_speed *= 0.9
