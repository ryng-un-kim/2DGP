from pico2d import *

# Game object class here


class Boy():
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class Grass():
    def __init__(self):
        pass

    def draw(self):
        pass


class Ball21():
    def __init__(self):
        pass

    def draw(self):
        pass


class Ball42():
    def __init__(self):
        pass

    def draw(self):
        pass


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
grass = Grass()
running = True;
# game main loop code

# finalization code
close_canvas()