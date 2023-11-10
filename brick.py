from turtle import Turtle
import random

COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "gray"]

class Brick(Turtle):

    def __init__(self,x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(x_cor, y_cor)
        self.bricks = []






    def lane(self, y_cor):
        for i in range(-450, 450, 63):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)


    def create_screen(self):
        for i in range(0, 280, 28):
            self.lane(i)



