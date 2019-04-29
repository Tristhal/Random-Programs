#graphics1.py
from pygame import *
from random import *
screen=display.set_mode((1000,800))
screen.fill((0,0,0))
running=True
while running:
#############################################################################################################################################################################################################################################
    clock=time.Clock()
    clock.tick(10)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
#############################################################################################################################################################################################################################################
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    for i in range(0,len(keys)):
        if keys[i]==1:
            print(i)
    display.flip()
quit()
