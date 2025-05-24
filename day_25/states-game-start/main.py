import pandas
import turtle

screen=turtle.Screen()

screen.title("States Game")
image= "indian_states.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("list_of_states_in_india-28j.csv")
states=data.State.tolist()
guessed_state=[]
while(len(guessed_state)<29):
    answer=screen.textinput(f"{len(guessed_state)}/28 states guessed","Guess the states of india").title()


    if answer in states and answer not in guessed_state:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data= data[data.State==answer]
        guessed_state.append(answer)
        t.goto(int(state_data.x),int(state_data.y))

        t.write(state_data.State.item())

        print(guessed_state)



screen.exitonclick()