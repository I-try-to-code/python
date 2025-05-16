from turtle import Turtle
MOV_DIST=20
POS= [(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT= 180
RIGHT=0


class Snake:

    def __init__(self):
        self.segm=[]
        self.create_snake()
        self.head=self.segm[0]


    def create_snake(self):
        for i in POS:
            seg = Turtle()
            seg.penup()
            seg.shape("square")
            seg.color("White")
            seg.goto(i)

            self.segm.append(seg)

    def move(self):
        for i in range(len(self.segm)-1,0,-1):
            new_x=self.segm[i-1].xcor()
            new_y= self.segm[i - 1].ycor()
            self.segm[i].goto(new_x,new_y)
        self.head.forward(MOV_DIST)

    def up(self):
        if( self.head.heading()!=DOWN):
            self.head.setheading(UP)
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)
    def lt(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    def rt(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
