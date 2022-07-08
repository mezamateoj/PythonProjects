from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fd():
    tim.fd(10)

def move_bd():
    tim.backward(10)

def move_r():
    tim.right(45)

def move_l():
    tim.left(45)

def clear():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(move_fd, 'w')
screen.onkey(move_bd, 's')
screen.onkey(move_r, 'd')
screen.onkey(move_l, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()
