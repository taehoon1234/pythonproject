import turtle as t
import random 
import time

t.bgcolor("lightblue")
t.setup(500,700)

player=t.Turtle()
player.shape("square")
player.shapesize(1,5)
player.up()
player.speed(0)
player.goto(0,-270)
