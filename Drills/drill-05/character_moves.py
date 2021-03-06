from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def move_from_xy1_to_xy2():  # 203, 503 -> 132, 243
    x, y = 203, 503
    frame = 0
    while x > 132:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
    while y > 243:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()


def move_from_xy2_to_xy3():  # 132, 243 -> 535, 470
    x, y = 132, 243
    frame = 0
    while x < 535:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while y < 470:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()


def move_from_xy3_to_xy4():  # 535, 470 -> 477, 203
    x, y = 535, 470
    frame = 0
    while x > 477:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
    while y > 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()


def move_from_xy4_to_xy5():  # 477, 203 -> 715, 136
    x, y = 477, 203
    frame = 0
    while x < 715:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while y > 136:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()


def move_from_xy5_to_xy6():  # 715, 136 -> 316, 225
    x, y = 715, 136
    frame = 0
    while x > 316:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
    while y < 225:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()


def move_from_xy6_to_xy7():  # 316, 225 -> 510, 92
    x, y = 316, 225
    frame = 0
    while x < 510:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while y > 92:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()


def move_from_xy7_to_xy8():  # 510, 92 -> 692, 518
    x, y = 510, 92
    frame = 0
    while x < 692:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while y < 518:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()


def move_from_xy8_to_xy9():  # 692, 518 -> 682, 336
    x, y = 692, 518
    frame = 0
    while x > 682:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
    while y > 336:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y -= 5
        delay(0.01)
        get_events()


def move_from_xy9_to_xy10():  # 682, 336 -> 712, 349
    x, y = 682, 336
    frame = 0
    while x < 712:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while y < 349:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()


def move_from_xy10_to_xy1():  # 712, 349 -> 203, 503
    x, y = 712, 349
    frame = 0
    while x > 203:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
    while y < 503:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        y += 5
        delay(0.01)
        get_events()


def move_character():
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


while True:
    move_character()

close_canvas()

