import time
from turtle import Screen
from snake import Snake
from food import Food

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.lt,"Left")
screen.onkey(snake.rt,"Right")

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.lt,"a")
screen.onkey(snake.rt,"d")


sta=True
while sta:
    time.sleep(0.2)
    snake.move()
    screen.update()

    if snake.head.distance(food)<15:
        print("eaten")
        food.eaten()










screen.exitonclick()