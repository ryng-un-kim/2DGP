from pico2d import *
import random
# Game object class here


class Boy():
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Grass():
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Ball21():
    def __init__(self):
        self.x, self.y = random.randint(100, 600), 600
        self.image = load_image('ball21x21.png')
        self.draw()

    def update(self):
        self.y -= 5
        if self.y < 50:
            self.y = 50

    def draw(self):
        self.image.draw(self.x, self.y)


class Ball41():
    def __init__(self):
        self.x, self.y = random.randint(100, 600), 600
        self.image = load_image('ball41x41.png')
        self.draw()

    def update(self):
        self.y -= random.randint(1, 5)
        if self.y < 50:
            self.y = 50

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code


open_canvas()
boy = Boy()
s_ball = Ball21()
b_ball = Ball41()
grass = Grass()
running = True;
# game main loop code


while running:
    handle_events()
    boy.update()
    s_ball.update()
    b_ball.update()
    clear_canvas()
    grass.draw()
    boy.draw()
    s_ball.draw()
    b_ball.draw()
    update_canvas()
    delay(0.05)

# finalization code
close_canvas()