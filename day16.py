from turtle import Turtle, Screen

timmy = Turtle()
window = Screen()
window.title('Welcome Mateo')

timmy.color('coral')
timmy.shape('turtle')
timmy.circle(50)
timmy.forward(50)
timmy.right(90)
timmy.forward(100)
timmy.circle(50)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.circle(50)
timmy.forward(100)
timmy.right(90)
timmy.forward(50)
timmy.right(90)
timmy.circle(100)
timmy.right(180)
timmy.circle(100)

#print(timmy.forward(50))
print(window.canvheight) # this is an attribute

window.exitonclick() # this is a method

