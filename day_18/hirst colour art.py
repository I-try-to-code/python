import random

import colorgram
from turtle import Screen, Turtle
import random
timmy= Turtle()
screen=Screen()
screen.colormode(255)
colors = colorgram.extract('./img.png', 30)
lis=[]
for colour in colors:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    lis.append((r, g, b))
timmy.penup()
timmy.setheading(225)
timmy.forward(390)
timmy.setheading(0)

for i in range(1,100):
    timmy.dot(20,random.choice(lis))
    timmy.forward(50)

    if i%10==0:
        timmy.setheading(50)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(550)
        timmy.setheading(0)



screen.exitonclick()



