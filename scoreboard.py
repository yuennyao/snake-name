from turtle import Turtle
from food import Food
import random

# Declare constant
ALIGNMENT = "center"
FONT = ("Courier", 18, "italic")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        # allow player to start playing again
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, ALIGNMENT, FONT)




