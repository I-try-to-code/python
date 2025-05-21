from turtle import Screen
from paddle import Paddle
from ball import Ball
ball= Ball()
import time
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PING PONG")
pad= Paddle()
screen.listen()
screen.onkeypress(pad.up1,"w")
screen.onkeypress(pad.down1,"s")
screen.onkeypress(pad.up2,"Up")
screen.onkeypress(pad.down2,"Down")
gamee=True
while gamee:
    time.sleep(0.01)
    ball.move()
    screen.update()
    #detecting collision with paddle
    if ball.ball.distance(pad.pad2)<50 and ball.ball.xcor()>320 or ball.ball.distance(pad.pad1)<50 and ball.ball.xcor()<-320:
        ball.bounce_paddle()





screen.exitonclick()











screen.exitonclick()