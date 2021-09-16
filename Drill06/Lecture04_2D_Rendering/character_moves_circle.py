from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=300
rad=0
def go1(x,y,rad):
    x=x+math.cos(rad/360*2*math.pi)*300
    y=y+math.sin(rad/360*2*math.pi)*300
    character.draw_now(x,y)
    

while (rad<460):
    clear_canvas_now()
    grass.draw_now(400,30)
    go1(x,y,rad)
    rad=rad+1
    if(rad>360):
        rad=0
    delay(0.01)
    
close_canvas()
