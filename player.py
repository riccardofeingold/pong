from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.draw(position)

    def draw(self, position):
        self.penup()
        self.shape("square")
        self.color("white")
        # initially a square comes with size 20x20; stretch_wid is a factor that is multiplied with 20
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)
        pass

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        pass

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        pass
