from turtle import Screen
from player import Player
from car_manager import Cars
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)


tim = Player()
cars = Cars()
score = ScoreBoard()

screen.listen()
screen.onkey(tim.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # Detect the collision of turtle with car
    for car in cars.all_cars:
        if car.distance(tim) < 25:
            game_is_on = False
            score.game_over()

    # Detection of turtle reaching the other side
    if tim.atfinishline():
        tim.reset()
        cars.increase()
        score.increase_score()



screen.exitonclick()
