import turtle
import random
timmy = turtle.Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)
for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)

   
   
   
screen = turtle.Screen()
screen.exitonclick()

