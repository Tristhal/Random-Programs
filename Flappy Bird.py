from pygame import *
from random import *
screen=display.set_mode((800,600))
running=True
cx,cy=400,500
changex=0
changey=0
rects=[]
counter=0
counter2=1
def moveRect(changex,changey,cx,cy):
    acceleration=.20
    brakes=.15
    brakesy=.5
    if 1==keys[119] and keydown==True:
        changey-=12
    if 1==keys[97]:
        changex-=acceleration
    if 1==keys[100]:
        changex+=acceleration     
    if changex>0:
        changex-=brakes
    else:
        changex+=brakes
    changey+=brakesy
    if changey>7:
        changey=7
    if changey<-15 and changey<0:
        changey=-15
    if screen.get_at((int(cx)+5,int(cy)+9))!=(0,0,0,255):
        print("blah")
        changey=0
        cx=400
        cy=300
        print("YOU LOOSE Score:",(500-counter2//30)*counter2//1000*len(rects)//2)
    cx+=changex
    cy+=changey
    return changex,changey,cx,cy
def drawRect(cx,cy):
    draw.rect(screen,(255,255,255),(cx,cy,10,10))
def drawRects(rects):
    for i in range(0,len(rects)):
        rects[i][0]-=counter2//1000+1
        draw.rect(screen,rects[i][4],(rects[i][0],rects[i][1],rects[i][2],rects[i][3]))
    return rects
while running:
    if counter>=500-counter2//30:
        rects.append([800,0,50,600,(255,255,255)])
        rects.append([800,randint(100,400),50,randint(100,150),(0,0,0)])
        counter=0
    screen.fill((0,0,0))
    draw.line(screen,(255,255,255),(0,580),(800,580),40)
    rects=drawRects(rects)
    clock=time.Clock()
    clock.tick(60)
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
        if evnt.type==KEYDOWN:
            keydown=True
        mx, my=mouse.get_pos()
        mb=mouse.get_pressed()
        keys=key.get_pressed()
    changex,changey,cx,cy=moveRect(changex,changey,cx,cy)
    drawRect(cx,cy)
    keydown=False
    counter+=1
    counter2+=1
    display.flip()
quit()
