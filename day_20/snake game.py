import time
import turtle
from turtle import Screen, Turtle

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
segm=[]
pos=[(0,0),(-20,0),(-40,0)]
screen.tracer(0)

for i in pos:
    seg = Turtle()
    seg.penup()
    seg.shape("square")
    seg.color("White")
    seg.goto(i)

    segm.append(seg)


sta=True
while sta:
    time.sleep(0.2)
    for i in range(len(segm)-1,0,-1):
        new_x=segm[i-1].xcor()
        new_y= segm[i - 1].ycor()
        segm[i].goto(new_x,new_y)
    segm[0].forward(20)
    segm[0].left(20)

    screen.update()










screen.exitonclick()