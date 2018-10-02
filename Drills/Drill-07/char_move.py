from pico2d import*
import random

W, H = 1024, 768

open_canvas()

kpu_ground = load_image("kpu_ground.png")
character = load_image("animation_sheet.png")
Idle = load_image("character.png")

def character_random_move(p1, p2):
    frame = 0
    for i in range(0, 100+1, 10):
        t = i/100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        

while True:
    pass

close_canvas()