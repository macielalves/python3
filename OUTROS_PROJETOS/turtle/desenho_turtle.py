import turtle
from turtle import *
from math import *
from time import sleep

bgcolor('blue')


def casa(x, y, length=100):
    pensize(4)
    penup()
    goto(x, y)
    color('green')
    begin_fill()
    pendown()
    for i in range(4):
        forward(length)
        left(90)

    end_fill()
    penup()
    goto(x-(length//4), y+length)
    left(180)
    color('red')
    begin_fill()
    pendown()
    for i in range(3):
        left(-120)
        forward(length * 1.5)

    end_fill()
    penup()
    goto(x+length/1.6, y)
    color('brown')
    begin_fill()
    pendown()
    right(90)
    forward(length//3.5)
    left(90)
    forward(length//4)
    left(90)
    forward(length//3.5)
    end_fill()
    hideturtle()


def sol(x, y):
    color('yellow')
    speed(11)
    pensize(3)
    penup()
    goto(x, y)
    pendown()
    for i in range(180):
        forward(i)
        right(i)


def lua():
    penup()
    speed(22)
    bgcolor('black')
    noite = 200
    altura = 2
    for i in range(200):
        noite -= 20
        if noite > 0:
            altura += 10
        elif noite < -100:
            altura -= 10
        goto(noite, altura)
        color('cyan')
        begin_fill()
        pendown()
        circle(50)
        hideturtle()
        end_fill()
        sleep(0.5)
        clear()


casa(-100, -200, 200)
sol(350, 200)
# lua()

done()
