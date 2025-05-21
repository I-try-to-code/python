from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score=0
        with open("score.txt") as file:
            self.high_score= int(file.read())
        self.score=0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score = {self.score} High Score= {self.high_score}",False,"center",("Calibri",20,"normal"))

    def incr(self):
        self.clr_scr()
        self.score+=1
        self.write(f"Score = {self.score} High Score= {self.high_score}",False,"center",("Calibri",20,"normal"))

    def clr_scr(self):
        self.color("Black")
        self.write(f"Score = {self.score} High Score= {self.high_score}",False,"center",("Calibri",20,"normal"))
        self.color("White")


    def reset(self):
        self.clr_scr()
        if self.score>self.high_score:
            self.high_score=self.score
            with open("score.txt", "w") as file1:
                file1.write(f"{self.high_score}")

        self.score=0
        self.write(f"Score = {self.score} High Score= {self.high_score}",False,"center",("Calibri",20,"normal"))



