import turtle

def drunken_up_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def drunken_right_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def drunken_left_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def drunken_down_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()



def restart():
    turtle.reset()

turtle.shape("turtle")
turtle.onkeypress(drunken_up_move,"Up")
turtle.onkeypress(drunken_right_move,"Right")
turtle.onkeypress(drunken_left_move,"Left")
turtle.onkeypress(drunken_down_move,"Down")
turtle.onkeypress(restart,"Escape")
turtle.listen()


