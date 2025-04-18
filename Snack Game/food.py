from turtle import Turtle
import random


class Food(Turtle):  # Food has inherited the properties of Turtle class

    def __init__(self):
        super().__init__()
        # Methods inherited from the super class
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
