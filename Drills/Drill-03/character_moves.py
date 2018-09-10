from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def Xmove():
    x = 400
    
    while (x<780):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        x +=5
        delay(0.01)

    if (x==780):
        Ymove()
    

def Ymove():
    y = 90
    while (y<560):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(780, y)
        y +=5
        delay(0.01)
    if (y==0 or y==560):
        Xmove2()

def Xmove2():
    x=780
    while (x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 560)
        x -=5
        delay(0.01)
    if (x==0):
        Ymove2()

def Ymove2():
    y=560
    while (y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0, y)
        y -=5
        delay(0.01)
    if (y==90):
        Xmove3()

def Xmove3():
    x=0
    while (x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        x +=5
        delay(0.01)

    if (x==400):
        Cmove()


def Cmove(): 
   
    Pi=3.14
    a=Pi*3/2
    
    while (a<7/2*Pi):

        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(210*math.cos(a)+400,210*math.sin(a)+300)
        a +=0.05
        
        delay(0.01)
        if (a<7/2*Pi):
            continue
        Xmove()

        

    
Xmove()
close_canvas()

