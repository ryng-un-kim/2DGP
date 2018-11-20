import random
from pico2d import *
import game_world
import game_framework
import background

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y, self.fall_speed = random.randint(1300, 1600 + 1300), random.randint(800 ,600 + 800), 0

    def set_background(self, bg):
        self.bg = bg
        self.x -= self.bg.w / 2
        self.y -= self.bg.h / 2

    def get_bb(self):
        return self.x - self.bg.window_left, self.y - self.bg.window_bottom, self.x - self.bg.window_left + 10, self.y- self.bg.window_bottom+ 10

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

