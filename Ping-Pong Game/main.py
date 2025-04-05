from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0) #To turn off the animation

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(rpaddle.up, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.up, "w")
screen.onkey(lpaddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision of ball with top and bottom wall
    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.bounce_y()

    #Detect collision with both paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    #Detect missing of collision with rpaddle
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()


    # Detect missing of collision with lpaddle
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
