from pico2d import *
import game_world
import game_framework
import math
import random

PIXEL_PER_METER = (10.0/0.3)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

T = 0.5  # 주기
pi = 3.14  # 원주율
R = 3 * PIXEL_PER_METER  # M
w = (2*pi)/T  # 각속도 = 원 둘레 / 시간

class Ghost:
    image = None
    global T, pi, R, w
    def __init__(self, x = 400, y = 300, timer = 10):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dis = 0
        self.x1, self.y1 = 0, 0
        self.timer = timer

    def draw(self):
        pass

    def update(self):
        pass
