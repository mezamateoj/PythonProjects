import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(225)
#tt.colormode(225)
#screen.colormode(225)
def color_mode():
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    color = (r,g,b)
    return color

tim.speed('fastest')
tim.color(color_mode())
tim.circle(100)

screen = Screen()
screen.exitonclick()
