from turtle import Turtle, Screen
import random
timmy = Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
directions = [0, 90, 180, 270]
timmy.speed("fastest")
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.pensize(15)
    timmy.forward(30)
    timmy.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick()