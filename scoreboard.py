from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
