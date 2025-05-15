import turtle
import random
timmy= turtle.Turtle()

lis=['t1','t2','t3','t4','t5','t6','t7']




screen=turtle.Screen()



screen.setup(500,400)
user_bet= screen.textinput("make your bet","which turtle do you think will win?")
colors=["violet","indigo","blue","green","yellow","orange","red"]
y_pos= [-70,-40,-10,20,50,80,110]
for x in range(0,7):
    timmy.penup()
    timmy.color(colors[x])
    timmy.goto(x=-230,y=y_pos[x])





screen.exitonclick()