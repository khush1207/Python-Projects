# This is the code for extracting the colors from the image
# import colorgram
#
# rgb = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)
import turtle as t
import random
tim = t.Turtle()
tim.hideturtle()
screen = t.Screen()


tim.speed("fastest")
tim.penup()
t.colormode(255)

color_list = ["green","yellow","purple", "blue", "light green", "cyan", "red", "pink"]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numberofdots = 100

for i in range(1, numberofdots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
