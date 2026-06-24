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

        self.high_score = self.read_high_score()
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
            self.write_high_score()
        self.score = 0
        self.print_score()
    
    def read_high_score(self):
        with open("data.txt") as file:
            contents = int(file.read())
            return contents
    
    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
           
