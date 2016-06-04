#graphics_play_2.py
from pygame import *
from random import *
running=True
screen = display.set_mode((1280, 1000))
balls=[]
gravballs=[]
asteroids=[]
walls=[[0,0],[1270,0]]
cx,cy=640,500
def ball(mx,my,drawtrue):
    X=0
    Y=1
    YSPD=2
    XSPD=3
    Time=4
    if drawtrue==1:
        balls.append([mx,my,randint(-40,40),randint(-40,40),randint(2,5)])
    for i in range(0,len(balls)):
        balls[i][YSPD]+=1
        balls[i][X]+=balls[i][XSPD]
        balls[i][Y]+=balls[i][YSPD]
        balls[i][Time]-=1
    for i in range(len(balls)-1,-1,-1):
        if balls[i][Time]<=0:
            del balls[i]            
    for i in balls:
        draw.circle(screen,(255,220,40),(int(i[X]),int(i[Y])),2)
def gravball(mx,my,drawtrue):
    X=0
    Y=1
    YSPD=2
    XSPD=3
    if drawtrue==1:
        gravballs.append([mx,my,randint(-40,-10),randint(-40,40)])
    for i in range(0,len(gravballs)):
        gravballs[i][YSPD]+=1
        gravballs[i][X]+=gravballs[i][XSPD]
        gravballs[i][Y]+=gravballs[i][YSPD]
    for i in range(len(gravballs)-1,-1,-1):
        if gravballs[i][Y]>=1000:
            del gravballs[i]            
    for i in gravballs:
        draw.circle(screen,(50,100,50),(int(i[X]),int(i[Y])),2)

def asteroids():
    g=1
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    clock=time.Clock()
    clock.tick(100)
    screen.fill((0,0,0))
    if 1==keys[119]:
        cy-=10
    if 1==keys[115]:
        cy+=10
    if 1==keys[97]:
        cx-=10
    if 1==keys[100]:
        cx+=10
    if cx <= 11:
        cx=10
        ball(cx+5,cy+5,1)
        ball(cx+5,cy+5,1)
        ball(cx+5,cy+5,1)
        gravball(cx,cy,1)
    if cx>=1270:
        cx=1260
        ball(cx+5,cy+5,1)
        ball(cx+5,cy+5,1)
        ball(cx+5,cy+5,1)
        gravball(cx,cy,1)
    draw.rect(screen,(50,255,50),(cx,cy,10,10))
    ball(cx+5,cy+5,0)
    gravball(cx+5,cy+5,0)
    for i in walls:
        draw.rect(screen,(255,255,255),(i[0],i[1],10,1000))
    asteroids
    
    


    display.flip()
quit()
