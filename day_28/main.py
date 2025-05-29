from math import floor
from tkinter import *


from numpy.ma.core import count

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    countdows(300)
    # start a timer countdown
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdows(count):
    count_min= count%60
    count_max= floor(count/60)
    canvas.itemconfig(timer_text,text=f"{count_max}:{count_min}")
    if count>0:
        window.after(1000,countdows,count-1)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.title("Pomodoro Timer")
window.config(padx=100,pady=50,bg=YELLOW)
canvas= Canvas(height=240,width=224,bg=YELLOW,highlightthickness=0)
tom_image=PhotoImage(file="tomato.png")
title_lable= Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
title_lable.grid(column=1,row=0)
canvas.create_image(100, 112,image=tom_image)

timer_text=canvas.create_text(100,132,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button= Button(text="Start",font=(FONT_NAME,12,"bold"),command=start_timer)
start_button.grid(row=2,column=0)

reset_button= Button(text="Reset",font=(FONT_NAME,12,"bold"))

reset_button.grid(row=2,column=2)
check_mark=Label(text="✔️",fg=GREEN,bg=YELLOW,font=(FONT_NAME,19,"bold"))
check_mark.grid(row=3, column=1,)



window.mainloop()
