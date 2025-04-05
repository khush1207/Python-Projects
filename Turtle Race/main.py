#State and Instances

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Make your bet", prompt="Which color turtle do you think will win the race?. "
                                                     "The color turtles are from VIBGYOR")
print(bet)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y = [-100, -70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[i])
    all_turtles.append(new_turtle)

is_race_on = False
if bet:
    is_race_on = True

while is_race_on:

    for i in all_turtles:
        if i.xcor() > 210:
            winner = i.pencolor()
            if winner == bet:
                print("You win! CONGO")
                is_race_on = False
            else:
                print(f"You lose. Better luck next time! The winner is {winner} turtle")
                is_race_on = False
        step = random.randint(0,10)
        i.fd(step)


screen.exitonclick()
