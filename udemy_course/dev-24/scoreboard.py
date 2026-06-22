from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)

        self.high_score = 0
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} | High Score: {self.high_score}",
            move=False,
            align=ALIGNMENT,
            font=FONT,
        )

    def update_score(self):
        self.score += 1
        self.print_score()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.print_score()
