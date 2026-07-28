import turtle as t
import random
is_race_on = False
screen = t.Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [180, 150, 120, 90, 60 , 30]
turtle_list = []
screen.setup(width=1000, height=600)
for turtle_index in range(0,6):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-480, y=y_positions[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for Turtle in turtle_list:
        if Turtle.xcor() > 400:
            is_race_on =False
            winner = Turtle.pencolor()
            if winner == user_bet:
                print(f"you won the {winner} turtle is the winnner ")
            else:
                print(f"you lose the {winner} turtle is the winnner ")
        random_distance = random.randint(0, 10)
        Turtle.forward(random_distance)



















screen.exitonclick()
