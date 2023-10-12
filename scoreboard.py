from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.write(f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.update_high_score()
        self.goto(0,0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.write_score()