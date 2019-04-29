from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1200,800)) #
running=True                        #
cx,cy=400,300                       #
#####################################
y2=0
x2=0
while running:
    clock=time.Clock()
    clock.tick(100)
    keydown=False
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type==KEYDOWN:
            if evnt.key==K_SPACE:
                keydown=True
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    y=my
    x=mx
    for i in range(-75,75):
        draw.aaline(screen,(abs(i),abs(i),abs(i)),((x+i/20),y),((x2+i/20),y2))
    y2=y
    x2=x
    display.flip()
quit()
