from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(0, 250)
        self.write(arg=f"Score = {self.score} High score = {self.high_score} ", move=False, align="center", font=("Arial", 20, "normal"))

    def new_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.new_high_score()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        with open("high_score.txt") as file:
            self.high_score = file.read()
            self.high_score = int(self.high_score)
        self.write(arg=f"Score = {self.score} High score = {self.high_score} ", move=False, align="center",
                   font=("Arial", 20, "normal"))

