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
R = 3 * PIXEL_PER_METER  # 반지름
w = (2*pi)/T  # 각속도 = 원 둘레 / 시간

class Ghost:
    image = None
    global T, pi, R, w
    def __init__(self, x = 400, y = 300, count = 10):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dis = 0
        self.x1 = 0
        self.count = count
        self.timer2 = 0
        self.r = 0



    def draw(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if self.timer2 < 12:
            self.image.clip_composite_draw(int(self.frame) * 100, 300, 100,
                                       100, pi / 2 + self.r, '', self.x -15, self.y, 100, 100)
        if self.timer2 > 12:
            self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, (self.x + R*math.cos(self.x1)), (self.y + R*math.sin(self.x1)))

    def update(self):
        self.count -= 1
        self.timer2 = get_time()
        self.dis = w * game_framework.frame_time
        self.x1 += self.dis
        if self.timer2 < 12:
            self.r -= (pi/2)/300
        if self.count == 0:
            self.image.opacify(random.randint(0, 8) *0.1)
            self.count = 10


