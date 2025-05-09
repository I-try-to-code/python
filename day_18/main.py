from turtle import Turtle, Screen

timmy= Turtle()


screen= Screen()
timmy.shape("turtle")
timmy.color("blue")
import heroes
print (heroes.gen())
for i in range(7):
     timmy.forward(10)
     timmy.penup()
     timmy.forward(10)
     timmy.pendown()


screen.exitonclick()