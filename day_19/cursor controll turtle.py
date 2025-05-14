import turtle
import random
timmy= turtle.Turtle()
screen=turtle.Screen()
def forw():
    timmy.forward(10)

def bac():
    timmy.backward(10)

def lef():
    new_heading= timmy.heading()+5
    timmy.setheading(new_heading)

def rig():
    new_heading = timmy.heading() - 5
    timmy.setheading(new_heading)


screen.listen()
turtle.onkeypress(forw, "w")
turtle.onkeypress(bac, "s")
turtle.onkeypress(lef, "a")
turtle.onkeypress(rig, "d")


screen.exitonclick()