from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


open_canvas()

kpu_ground = load_image('kpu_ground.png')
character = load_image('animation_sheet.png')


def character_move(p1, p2):
    frame = 0
    for i in range(0, 100+1, 10):
        t = i/100
        x = (1-t)*p1[0] + t*p2[0]
        y = (1-t)*p1[1] + t*p2[1]
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if p1[0] > p2[0]:
            character.clip_draw(frame * 100, 1 * 1, 100, 100, x, y)
        if p1[0] < p2[0]:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.04)


size = 20
points = [(random.randint(100, 500), random.randint(150, 400)) for i in range(size)]
n = 1


while True:
    character_move(points[n-1], points[n])
    n = (n+1) % size


close_canvas()