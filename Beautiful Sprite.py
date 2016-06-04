from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1200,800)) #
running=True                        #
cx,cy=400,300                       #
#####################################
###
#Font
init()
myfont=font.SysFont("monospace", 20)
#Font
###
circles=[]
keydown=False
circlespawns=1
circlespawnspeed=.01
###
#MoveCharacters
charactercolour=(150,30,70)
changex=0
changey=0
changex2=0
changey2=0
brakes=.5
acceleration=1
#MoveCharacters
###
def moveCharacter(cx,cy,changex,changey):
    if cy>my:
        changey-=acceleration
    if cy<my:
        changey+=acceleration
    if cx>mx:
        changex-=acceleration
    if cx<mx:
        changex+=acceleration
    if cy+changey<0:
        changey=-changey
    elif cy+changey>screen.get_height():
        changey=-changey
        changex=-changex
    if cx+changex<0:
        changex=-changex
    elif cx+changex>screen.get_width():
        changex=-changex
    cx+=changex
    cy+=changey
    return cx,cy,changex,changey
def spawnGradientBubble(mx,my,circles):
    #xy=(randint(mx-100,mx+100),randint(my-100,my+100))
    xy=(mx,my)
    for i in range(1,15):
        circles.append([255,xy,i,i**.31])
    for i in range(15,100):
        circles.append([255-i*2,xy,i,i/8])
    return circles
def drawGradientBubble(circles):
    for i in range(len(circles)-1,-1,-1):
        if circles[i][0]-circles[i][3]<=0:
            del circles[i]
        else:
            draw.circle(screen,(circles[i][0],170,180),circles[i][1],circles[i][2])
            circles[i][0]-=circles[i][3]
    return circles
while running:
    clock=time.Clock()
    clock.tick(60)
    screen.fill((0,170,180))
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
    if keydown==True and circlespawns>0:
        circles=spawnGradientBubble(int(cx),int(cy),circles)
        circlespawns-=1
    cx,cy,changex,changey=moveCharacter(cx,cy,changex,changey)    
    ###  End Stuff  ###
    label=myfont.render("Bubbles:"+str(round(circlespawns,1)),1, (105,0,102))
    screen.blit(label,(10, 10))
    circles=drawGradientBubble(circles)
    circlespawns+=circlespawnspeed
    draw.circle(screen,charactercolour,(int(cx),int(cy)),5)
    ### END END END ###
    display.flip()
quit()
