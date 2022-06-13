from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Razor 1911 Font", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player_one = 0
        self.score_player_two = 0
        self.hideturtle()
        self.color("white")
        self.setposition(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score_player_one}    {self.score_player_two}", align=ALIGNMENT, font=FONT)
