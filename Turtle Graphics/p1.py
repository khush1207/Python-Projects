from turtle import Turtle, Screen
import random
timmy = Turtle()
timmy.shape("turtle")

for i in range(3, 11):
    angle = 360/i
    c = ["red", "blue", "cyan", "purple", "violet", "black", "pink", "yellow", "orange", "brown"]
    timmy.color(random.choice(c))
    for n in range(i):
        timmy.fd(100)
        timmy.right(angle)


screen = Screen()
screen.exitonclick()