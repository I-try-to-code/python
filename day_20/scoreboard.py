from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score = {self.score}",False,"center",("Calibri",20,"normal"))

    def incr(self):
        self.clr_scr()
        self.score+=1
        self.write(f"Score = {self.score}",False,"center",("Calibri",20,"normal"))

    def clr_scr(self):
        self.color("Black")
        self.write(f"Score = {self.score}",False,"center",("Calibri",20,"normal"))
        self.color("White")

    def game_over(self):
        self.clr_scr()
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ("Calibri", 20, "normal"))
