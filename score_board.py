from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color("red")
        self.penup()
        self.hideturtle()

        #score
        self.l_score = 0
        self.r_score = 0
        self.update_score()






    def update_score(self):

        # to not overlap the score
        self.clear()

        # left of the screen and top ---> text
        self.goto(-100,220)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal") )  # score of the left paddle player
        self.goto(100,220)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))  # score of the right paddle player

        #point
    def l_point(self):
        self.l_score += 1
        self.update_score()

        #point
    def r_point(self):
        self.r_score += 1
        self.update_score()









