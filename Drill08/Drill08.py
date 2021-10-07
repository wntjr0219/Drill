import turtle
import random
import math


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())

# 직선의 방정식


#파라미터 방정식
def draw_line(p1):
    
    x1, x2 = p1
    a=x1-x2
    b=x2
    c=x1/x2



    for i in range(0, 100+1, 5
    ):
        t = i/100
        x = math.cos(t)*abs(a) + math.cos(abs(c)*t-1)*b
        y = math.sin(t)*abs(a) + math.sin(abs(c)*t-1)*b
        draw_point((x,y))


    pass

prepare_turtle_canvas()

p1 = 400,100
p2 = 100, 25
p3 = -400, -100
p4 = -100, -25


draw_line(p1)
draw_line(p2)
draw_line(p3)
draw_line(p4)

turtle.done()