import turtle as t
import random
import colorgram 
timmy = t.Turtle()
timmy.speed("fastest")
t.colormode(255)
def colors_random():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


for _ in range(80):
    timmy.color(colors_random())
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 5)
    timmy.circle(100)

screen = t.Screen()
screen.exitonclick()