FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.__print_level()

    def __print_level(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.__print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

