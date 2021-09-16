from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=0
y=90

def go1(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
def go2(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
def go3(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
def go4(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
while(1):
    while (x<800):
        go1(x,y)
        x=x+2
        
    while (y<600):
        go2(x,y)
        y=y+2

    while (x>0):
        go3(x,y)
        x=x-2

    while (y>90):
        go4(x,y)
        y=y-2
