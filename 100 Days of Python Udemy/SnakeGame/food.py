from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        x_random = random.randint(-260, 260)
        y_random = random.randint(-260, 260)
        self.goto(x_random, y_random)
        self.refresh()

    def refresh(self):
        x_random = random.randint(-260, 260)
        y_random = random.randint(-260, 260)
        self.goto(x_random, y_random)