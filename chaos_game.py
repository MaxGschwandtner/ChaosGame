from turtle import Turtle, Screen
import random
from math import sqrt, cos, sin, pi

screen = Screen()
t = Turtle()
screen.setup(600, 540)
t.hideturtle()
vertices = []

def compute_vertices(v, r):
    angle = 360 / v
    if v % 2 == 1:
        phi = 90
        for i in range(v):
            x = r*cos(phi*pi/180)
            y = r*sin(phi*pi/180)
            vertices.append((x, y))
            phi = phi + angle
    else:
        phi = angle/2
        for i in range(v):
            x = r*cos(phi*pi/180)
            y = r*sin(phi*pi/180)
            vertices.append((x, y))
            phi = phi + angle

    return vertices


def polygon(v):
    t.penup()
    t.goto(vertices[0])
    t.pendown()
    for i in range(v):
        t.goto(vertices[i])
    t.goto(vertices[0])


def start():
    start_x = random.randint(-200, 200)
    start_y = random.randint(-200, 200)
    t.penup()
    t.goto(start_x, start_y)
    t.dot(3, "red")


def draw(v, same_vertex=False):
    early_ver = -1
    while True:
        ver = random.randint(0, v - 1)
        if same_vertex == True:
            while ver == early_ver:
                ver = random.randint(0, v - 1)
        vertex = vertices[ver]
        t_pos = t.position()
        t.setheading(t.towards(vertex))
        step = sqrt((vertex[0] - t_pos[0])**2 + (vertex[1] - t_pos[1])**2) / 2
        t.fd(step)
        t.dot(3)
        early_ver = ver

def animation(v, r):
    compute_vertices(v, r)
    screen.tracer(False)
    polygon(v)
    screen.tracer(True)
    start()
    t.speed(100000)
    draw(v, True)

animation(4, 300)
screen.mainloop()
