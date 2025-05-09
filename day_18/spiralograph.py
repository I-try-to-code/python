from turtle import Screen, Turtle
import random
timmy= Turtle()
screen=Screen()
screen.colormode(255)

screen= Screen()
timmy.speed("fastest")
timmy.pensize(3)
for i in range(365):
    red = random.randint(0, 225)
    blue = random.randint(0, 225)
    green = random.randint(0, 225)
    timmy.color((red, blue, green))
    timmy.circle(100)
    timmy.left(5)
screen.exitonclick()