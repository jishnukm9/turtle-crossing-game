from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}',align='left',font=('Courier',20,'bold'))


    def level_increment(self):
        self.level+=1
        self.update_score()


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=('Courier',30,'bold'))