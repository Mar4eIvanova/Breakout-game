from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(250, 270)
        self.write(f"Score: {self.score}", align="right", font=("Courier", 40, "normal"))

    def point(self):
        self.score += 1
        self.update()

