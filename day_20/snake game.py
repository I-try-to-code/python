import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake=Snake()
food=Food()
scoreb=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.lt,"Left")
screen.onkey(snake.rt,"Right")

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.lt,"a")
screen.onkey(snake.rt,"d")


gamee=True
while gamee:
    time.sleep(0.2)
    snake.move()
    screen.update()



    #detect collision with foodd
    if snake.head.distance(food)<15:
        print("eaten")
        snake.extend()
        food.eaten()
        scoreb.incr()

    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        scoreb.game_over()
        gamee=False

    # detect collision with bodyy
    for i in snake.segm:
        if i==snake.head:
            pass
        else:
            if snake.head.distance(i)<10:
                scoreb.game_over()
                gamee=False










screen.exitonclick()