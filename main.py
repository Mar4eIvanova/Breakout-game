import turtle
import time
from paddle import Paddle
from ball import Ball
from brick import Brick
from score import Score
from lives import Lives

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Mariya's Breakout")
screen.setup(width=950, height=700)
paddle = Paddle((0, -300))

ball = Ball()
lives = Lives()
score = Score()


screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.listen()

brick = Brick(x_cor=0, y_cor=0)
brick.hideturtle()
turtle.tracer(0, 0)
brick.create_screen()
game_on = True

def game():
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

def wall_collision():
    if ball.xcor() < -450 or ball.xcor() > 450:
        ball.wall_bounce()
    elif ball.ycor() > 300:
        ball.bounce()


def paddle_collision():
    if ball.distance(paddle) < 60 and ball.ycor() < -290:
        ball.bounce()

def brick_collision():
    for b in brick.bricks:
        if ball.distance(b) < 30:
            brick.bricks.remove(b)
            b.hideturtle()
            score.point()


def check_for_lives():
    if ball.ycor() < -320:
        lives.minus_live()
        lives.update()
        ball.resset_position()


while game_on:
    game()
    paddle_collision()
    wall_collision()
    brick_collision()
    score.update()
    check_for_lives()

    if lives.lives == 0:
        turtle.goto(350, 0)
        turtle.color("#7CFC00")
        turtle.write(f"Game Over!!!\nYour Score: {score.score}", align="right", font=("Courier", 70, "bold"))
        break























screen.exitonclick()
