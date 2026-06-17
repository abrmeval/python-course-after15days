from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.set_starting_position()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def set_starting_position(self):
        self.setposition(STARTING_POSITION)
        self.setheading(90)

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

