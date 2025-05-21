from turtle import Turtle
positions = [(-350, 0), (350, 0)]
class Paddle:
    def __init__(self):
        self.paddles = []
        for pos in positions:
            self.create_paddle(pos)

        self.pad1 = self.paddles[0]
        self.pad2 = self.paddles[1]

    def create_paddle(self, position):
        pad = Turtle("square")
        pad.shapesize(stretch_wid=1, stretch_len=5)
        pad.color("white")
        pad.penup()
        pad.goto(position)
        pad.setheading(90)
        self.paddles.append(pad)

    def up1(self):
        if self.pad1.ycor() < 250:
           self.pad1.forward(20)

    def down1(self):
        if self.pad1.ycor() > -250:
            self.pad1.backward(20)

    def up2(self):
        if self.pad2.ycor() < 250:
            self.pad2.forward(20)

    def down2(self):
        if self.pad2.ycor() > -250:
            self.pad2.backward(20)
