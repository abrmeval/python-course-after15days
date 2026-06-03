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

        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()
    
    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)


