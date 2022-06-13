from turtle import Turtle


class Ball(Turtle):
    def __init__(self, velocity_x, velocity_y):
        super().__init__()
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.game_is_on = True
        self.draw()

    def draw(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setposition = (0, 0)
        pass

    def bounce_y(self):
        self.velocity_y *= -1

    def bounce_x(self):
        self.velocity_x *= -1

    def collision_with_top_bottom(self):
        # Collision with top and bottom
        if self.ycor() > 290 or self.ycor() < -280:
            self.bounce_y()

    def increase_speed(self):
        self.velocity_x *= 1.5

    def collision_with_paddle(self, l_paddle, r_paddle):
        # Collision with paddle
        if self.distance(r_paddle) < 50 and self.xcor() > r_paddle.xcor() - 20 or self.distance(
                l_paddle) < 50 and self.xcor() < l_paddle.xcor() + 20:
            self.increase_speed()
            self.bounce_x()

    def move(self):
        self.collision_with_top_bottom()
        new_x = self.xcor() + self.velocity_x
        new_y = self.ycor() + self.velocity_y
        self.goto(new_x, new_y)
        pass

    def reset_position(self):
        self.velocity_x = 2
        self.velocity_y = 2
        self.goto(0, 0)
        self.bounce_x()
