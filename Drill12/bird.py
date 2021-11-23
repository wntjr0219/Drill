import random
from pico2d import *
from boy import ACTION_PER_TIME, FRAMES_PER_ACTION
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
FLY_SPEED_KMPH = 30.0  # Km / Hour
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

min_x = 50
max_x = 800 - 50
dir = random.randint(0, 1)

class Bird:
    image = None

    def __init__(self):
        global min_x, max_x
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.frame = 0
        self.x, self.y = random.randint(min_x, max_x), random.randint(40 + 50, 600 - 50)

    def update(self):
        global min_x, max_x, dir
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        if dir == 1:
            velocity = FLY_SPEED_PPS 
        else:
            velocity = FLY_SPEED_PPS * -1
        if self.x <= min_x:
            velocity = FLY_SPEED_PPS
        elif self.x >= max_x:
            velocity = FLY_SPEED_PPS * -1
        
        self.x += velocity * game_framework.frame_time
        self.x = clamp(min_x, self.x, max_x)


    def draw(self):
        global min_x, max_x, dir
        if dir == 1:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
           self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 100, 3.141592 / 1.3, '', self.x, self.y, 100, 100)
    