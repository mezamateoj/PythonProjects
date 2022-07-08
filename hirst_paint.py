import turtle as t
from turtle import Screen
import random
import colorgram

# colors = colorgram.extract('damien.webp', 30)

# rgb_colors = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color = [(250, 246, 243), (248, 245, 246), (212, 154, 97), (239, 246, 243), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (235, 240, 244), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), 
(239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81)]

t.colormode(255)
paint = t.Turtle()

def draw(space, x, y):
    for i in range(x):
        for j in range(y):
            new_color = random.choice(color)
            paint.dot(20, new_color)

            paint.forward(space)
        paint.backward(space * y)

        paint.right(90)
        paint.forward(space)
        paint.left(90)

paint.speed('fastest')
paint.penup()
paint.setx(-250)
paint.sety(200)
draw(50, 10, 10)
paint.hideturtle()

screen = Screen()
screen.exitonclick()