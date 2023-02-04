from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__() 
        self.number = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.write_score()
        self.hideturtle()
        

    def write_score(self):
        self.write(f'Score: {self.number}', align='center', font=('Arial', 18, 'normal'))



    def update_score(self):
        self.number += 1
        self.clear()
        self.write_score()
        

    def game_over(self):
        self.color('white')
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 20, 'normal'))


    