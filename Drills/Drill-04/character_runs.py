from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move():

    x = 0
    frame = 0
    while x < 800:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while x > 0:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
        if x == 0:
            move()


move()

close_canvas()

