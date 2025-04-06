from turtle import Turtle
import random

COLOR_OF_CARS = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]


class Cars:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = 5


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOR_OF_CARS))
            random_y = random.randint(-240, 240)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase(self):
        self.speed += 10
