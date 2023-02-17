from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Ping Pong')

paddle = Turtle()

paddle.color('white')
paddle.shape('square')
paddle.shapesize(5, 1)
paddle.setposition(350, 0)


screen.exitonclick()
