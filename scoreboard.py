from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")

with open(file='data.txt', mode='r') as file:
    contents = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.color('blue')
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def set_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='data.txt', mode='w') as file_w:
                file_w.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

