from pico2d import *
from random import randint
KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running

    events=get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if  event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running=False
    pass

def hand_move():
    global x,y
    global act
    global hand_x,hand_y

    hand_x, hand_y = randint(0,KPU_WIDTH), randint(0,KPU_HEIGHT)
    while hand_x==x and hand_y==y:
        if x<hand_x:
            act = 1

        elif x>hand_x:
            act = 0
        x,y = hand_x, hand_y


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
hand_x, hand_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
act=1
frame = 0

hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(hand_x, hand_y)
    character.clip_draw(frame * 100, 100 * act, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.01)

    handle_events()
    hand_move()

close_canvas()




