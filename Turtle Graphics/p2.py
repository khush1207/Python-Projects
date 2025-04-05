import turtle as t
import random

tim = t.Turtle()
tim.speed(0)
screen = t.Screen()
screen.screensize(2000, 1000)
tim.hideturtle()
tim.pensize(8)

#Generating a random color rather than selecting named colors from a list using pencolor() and RGB tuple
t.colormode(255)


def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c = (r, g, b)
    return c

for i in range(200):
    direction = [0,90,180,270]
    #Calling the randomcolor here to change the color for every movement
    tim.color(randomcolor())
    tim.forward(30)
    tim.setheading(random.choice(direction))