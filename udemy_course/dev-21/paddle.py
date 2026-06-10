from turtle import Turtle

MOVE_DISTANCE = 20
ORIENTATION = 90


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.setposition(position)
        self.setheading(ORIENTATION)

    def up(self):
        self.forward(MOVE_DISTANCE)


    def down(self):
        self.backward(MOVE_DISTANCE)
