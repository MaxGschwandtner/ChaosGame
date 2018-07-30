from turtle import Turtle, Screen
import random
from math import sqrt

screen = Screen()
t = Turtle()
screen.setup(600, 540)
t.hideturtle()
vertices = [(0, 206), (-200, -140), (200, -140)]

def triangle():
    t.penup()
    t.goto(0, 206)
    t.pendown()
    t.right(60)
    t.forward(400)
    t.right(120)
    t.forward(400)
    t.right(120)
    t.forward(400)

def start():
    start_x = 500
    start_y = 500
    while abs(start_y) + abs(start_x) > 180:
        start_x = random.randint(-200, 200)
        start_y = random.randint(-140, 206)

    t.penup()
    t.goto(start_x, start_y)


def draw():
    while True:
        v = random.randint(0, 2)
        vertex = vertices[v]
        t_pos = t.position()
        t.setheading(t.towards(vertex))
        step = sqrt((vertex[0] - t_pos[0])**2 + (vertex[1] - t_pos[1])**2) / 2
        t.fd(step)
        t.dot(3)

def animation():
    screen.tracer(False)
    triangle()
    screen.tracer(True)
    start()
    t.speed(1000)
    draw()

animation()
screen.mainloop()
