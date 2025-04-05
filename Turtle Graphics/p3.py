import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")


t.colormode(255)
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c = (r, g, b)
    return c

def draw(sizeofgap):
    for i in range(int(360/sizeofgap)):
        tim.color(randomcolor())
        tim.circle(100)
        tim.setheading(tim.heading() + sizeofgap)

draw(5)
