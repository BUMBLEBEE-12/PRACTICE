from turtle import Screen
from Paddle import Paddle
from ball import ball
import time 
from scoreboard import Scoreboard
screen = Screen()
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
game_on = True
screen.listen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
Ball = ball()
score = Scoreboard()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
while game_on:
    screen.update()
    Ball.move()
    time.sleep(0.1)
    if Ball.ycor() > 250 or Ball.ycor() < -250:
        Ball.bounce_y()
    if Ball.distance(r_paddle) < 50 and Ball.xcor() > 330 or Ball.distance(l_paddle) < 50 and Ball.xcor() < -330:
        Ball.bounce_x()
    if Ball.xcor() > 380:
        Ball.goto(0, 0)
        Ball.bounce_x()
        score.l_point()
    if Ball.xcor() < -380:
        Ball.goto(0, 0)
        Ball.bounce_x() 
        score.r_point()
screen.exitonclick()