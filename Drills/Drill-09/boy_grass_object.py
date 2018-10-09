from pico2d import *

# Game object class here


class Boy():
    pass

class Grass():
    pass

class Ball21():
    pass

class Ball42():
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

# game main loop code

# finalization code