from turtle import Turtle, Screen
import random


is_race_on = False
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Bets', prompt='Who is going to win, Enter a color:')
all_turtles = []

cord = 40
for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.fillcolor(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-140 + cord)
    cord += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 220:
            is_race_on = False
            winning_color = t.fillcolor()

            if winning_color == user_bet:
                print(f'You won, the turtle was color {winning_color}')
            else:
                print(f'You lost, the winner was {winning_color}')


        rand_distance = random.randint(0, 15)
        t.forward(rand_distance)


screen.exitonclick()