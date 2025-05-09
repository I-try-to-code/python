from turtle import Turtle, Screen
import random
timmy= Turtle()


screen= Screen()
timmy.shape("turtle")
timmy.color("blue")
screen.colormode(255)
def random_walk():
     while True:
          x= random.randint(0,1)
          red = random.randint(0, 225)
          blue = random.randint(0, 225)
          green = random.randint(0, 225)
          if x==0:
               timmy.left(90)
               timmy.forward(20)
          else:
               timmy.right(90)
               timmy.forward(20)
          timmy.color((red,blue,green))
random_walk()
screen.exitonclick()