import turtle as t
import random 
import time

def right():
    if player.xcor() < 200:
        player.forward(10)

def left():
    if player.xcor() > -200:
        player.backward(10)



t.bgcolor("lightblue")
t.setup(500,700)

player=t.Turtle()
player.shape("square")
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0,-270)


# ball
ball= t.Turtle()
ball.shape("circle")
ball.shapesize(1.3)
ball.up()
ball.speed(0)
ball.color("white")





t.listen()
t.onkeypress(right,"Right")
t.onkeypress(left,"Left")


