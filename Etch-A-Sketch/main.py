from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.speed("fastest")


def movefd():
    tim.fd(10)


def movebk():
    tim.backward(10)


def counterclock():
    tim.left(10)


def clock():
    tim.right(10)


def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=movefd)
screen.onkey(key="s", fun=movebk)
screen.onkey(key="a", fun=counterclock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clearscreen)

screen.exitonclick()