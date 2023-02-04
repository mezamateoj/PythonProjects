from turtle import Turtle

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    move_distance = 20
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)
           
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def move(self):
        for seg_number in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.head.forward(self.move_distance)


    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    