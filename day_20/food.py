from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        ranx= random.randint(-280,280)
        rany= random.randint(-280,280)
        self.goto(ranx,rany)

    def eatenn(self):
        ranx = random.randint(-280, 280)
        rany = random.randint(-280, 280)
        self.goto(ranx, rany)
