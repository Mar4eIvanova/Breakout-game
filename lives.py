from turtle import Turtle


class Lives(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lives = 5
        self.update()

    def update(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f"Lives: {self.lives}", align="right", font=("Courier", 40, "normal"))

    def minus_live(self):
        self.lives -= 1
        self.update()
