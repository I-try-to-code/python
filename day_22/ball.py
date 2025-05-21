from turtle import Turtle
import paddle
class Ball:
    def __init__(self):

        self.ball = Turtle("circle")
        self.create_ball()
        self.x=10
        self.y=10

    def create_ball(self):

        self.ball.color("white")
        self.ball.penup()

    def move(self):
        self.ball_bounce()
        xco=self.ball.xcor()+self.x
        yco=self.ball.ycor()+self.y
        self.ball.goto(xco,yco)

    def ball_bounce(self):
        if self.ball.ycor() > 280:
            if self.x == 10 and self.y == 10:
                self.y = -10
                pass
            elif self.x == -10 and self.y == 10:
                self.y = -10

        if self.ball.ycor() < -280:
            if self.x == -10 and self.y == -10:
                self.y = +10
                pass

            elif self.x == 10 and self.y == -10:
                self.y = 10

    def bounce_paddle(self):
        self.x*=-1



