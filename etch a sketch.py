from turtle import *
timy=Turtle()
screen=Screen()


def move_forward():
    timy.forward(10)


def move_backward():
    timy.backward(10)


def move_right():
    timy.right(10)


def move_left():
    timy.left(10)


def clear():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()


screen.listen()
screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(move_left, "Up")
screen.onkey(move_right, "Down")
screen.onkey(clear, "c")
screen.exitonclick()