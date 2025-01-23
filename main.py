from turtle import Turtle, Screen
from paddle import Paddle

L_PAD_CORD = (-350, 0)
R_PAD_CORD = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(L_PAD_CORD)
r_paddle = Paddle(R_PAD_CORD)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()