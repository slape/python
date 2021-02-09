from turtle import *

hideturtle()
color('black', 'magenta')


def left_turn():
    for i in range(10):
        forward(15)
        left(9)


def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn()
    end_fill()
    left(90)


def flower():
    for i in range(5):
        petal()
        right(365/5)


def buquet():
    for i in range(5):
        flower()
        penup()
        forward(200)
        pendown()


buquet()
