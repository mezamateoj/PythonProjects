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
#directions = [0, 90, 180, 270]

#tt.bgcolor('black')
#tim.pensize(15)

# for i in range(200):
#     tim.color(color_mode())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
# import random
# import turtle

# from turtle import Turtle
# turtle.colormode(255)
# tim = Turtle()
# tim.speed("fastest")
# direction = [90,  270]
# #colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pensize(5)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# while True:
#     move = random.choice(direction)
#     tim.forward(40)
#     tim.color(random_color())
#     tim.left(move)
