from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time

# setup screen
screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("My Pong")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball(velocity_x=2, velocity_y=2)
l_player = Player(position=(-450, 0))
r_player = Player(position=(450, 0))

screen.listen()
screen.onkey(r_player.move_up, "Up")
screen.onkey(r_player.move_down, "Down")
screen.onkey(l_player.move_up, "w")
screen.onkey(l_player.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    ball.collision_with_paddle(l_paddle=l_player, r_paddle=r_player)

    if ball.xcor() > 480:
        l_player.score += 1
        scoreboard.score_player_one = l_player.score
        ball.reset_position()

    if ball.xcor() < -490:
        r_player.score += 1
        scoreboard.score_player_two = r_player.score
        ball.reset_position()

    scoreboard.update_score()
    game_is_on = ball.game_is_on

screen.exitonclick()
