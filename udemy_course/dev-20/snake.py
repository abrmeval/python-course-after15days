from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.__snake_start()
        self.head = self.squares[0]

    def __create_square(self):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        self.squares.append(square)
        return square

    def __snake_start(self):
        prev_square = self.__create_square()
        for _ in range(2):
            x, y = prev_square.position()
            new_square = self.__create_square()
            new_square.goto(x - MOVE_DISTANCE, y)
            prev_square = new_square

    def move(self):
        size = len(self.squares)
        for x in range(size - 1, 0, -1):
            self.squares[x].goto(self.squares[x - 1].position())

        self.head.forward(MOVE_DISTANCE)


    def add_square(self):
        last_square = self.squares[-1]
        new_square = self.__create_square()
        x, y = last_square.position()
        orientation = self.head.heading()

        if orientation == 0:
            new_square.goto(x - MOVE_DISTANCE, y)
        elif orientation == 90:
            new_square.goto(x, y - MOVE_DISTANCE)
        elif orientation == 180:
            new_square.goto(x + MOVE_DISTANCE, y)
        else:
            new_square.goto(x, y + MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
