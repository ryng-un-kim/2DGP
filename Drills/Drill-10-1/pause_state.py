import game_framework
from pico2d import *
import main_state


name = "PauseState"

image = None


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass