from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_from_xy1_to_xy2():
    x, y = 203, 503
    frame = 0
    while x > 132 and y > 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 1
        y -= 1
        delay(0.02)
        get_events()


def move_from_xy2_to_xy3():
    pass


def move_from_xy3_to_xy4():
    pass


def move_from_xy4_to_xy5():
    pass


def move_from_xy5_to_xy6():
    pass


def move_from_xy6_to_xy7():
    pass


def move_from_xy7_to_xy8():
    pass


def move_from_xy8_to_xy9():
    pass


def move_from_xy9_to_xy10():
    pass


def move_from_xy10_to_xy1():
    pass


while True:
    move_from_xy1_to_xy2()
    move_from_xy2_to_xy3()
    move_from_xy3_to_xy4()
    move_from_xy4_to_xy5()
    move_from_xy5_to_xy6()
    move_from_xy6_to_xy7()
    move_from_xy7_to_xy8()
    move_from_xy8_to_xy9()
    move_from_xy9_to_xy10()
    move_from_xy10_to_xy1()

close_canvas()

