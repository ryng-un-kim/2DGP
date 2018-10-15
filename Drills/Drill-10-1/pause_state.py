import game_framework
from pico2d import *
import main_state

name = "PauseState"

image = None
frame = 0


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)


def update():
    global frame
    delay(0.4)
    frame = (frame + 1) % 2


def draw():
    global image
    global frame
    clear_canvas()
    image.clip_draw(frame*400, 0, 300, 300, 400, 300)
    main_state.boy.draw()
    main_state.grass.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:
                game_framework.pop_state()


def pause():
    pass


def resume():
    pass