from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((800,600)) #
running=True                        #
cx,cy,cz=400,300,0                  #
#####################################
###
#Font
init()
myfont=font.SysFont("monospace", 20)
choicelist=[i/1000 for i in range(-5000,5001)]
circles=[]
#Font
###
circles=[]
keydown=False
circlespawns=1
circlespawnspeed=.01
###
#MoveCharacters
charactercolour=(0,0,0)
changex=0
changey=0
changex2=0
changey2=0
brakes=.05
acceleration=1.2
#MoveCharacters
###
changez=15
def moveCharacter(cx,cy,changex,changey,changez,cz):
    changey+=1
    if 1==keys[119]:
        changey-=acceleration
    if 1==keys[115]:
        changey+=acceleration
    if 1==keys[97]:
        changex-=acceleration
    if 1==keys[100]:
        changex+=acceleration
    '''if changex>0:
        changex-=brakes
    else:
        changex+=brakes
    if changey>0:
        changey-=brakes
    else:
        changey+=brakes'''
    if cy+changey<0:
        changey=-changey/1.3
    elif cy+changey>screen.get_height():
        changey=-changey/1.3
    if cx+changex<0:
        changex=-changex/1.3
    elif cx+changex>screen.get_width():
        changex=-changex/1.3
    if cz+changez>100:
        changez=-changez
    elif cz+changez<-100:
        changez=-changez
    #changex+=choice([-1,-1,1,1,-1.5,-1.5,1.5,1.5])
    #changey+=choice([-1,-1,1,1,-1.5,-1.5,1.5,1.5])
    cx+=changex
    cy+=changey
    cz+=changez
    return cx,cy,changex,changey,changez,cz
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
z=5
clock=time.Clock()
while running:
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
    '''if keydown==True:#keydown==True and circlespawns>0:
        circles=spawnGradientBubble(int(cx),int(cy),circles)
        circlespawns-=1'''
    for i in range(0,len(circles)):
        circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5]=moveCharacter(circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5])
        screen.fill(charactercolour,(int(circles[i][0]),int(circles[i][1]),abs(int(circles[i][5]/5)),abs(int(circles[i][5]/5))))
    ###  End Stuff  ###
    '''label=myfont.render("Bubbles:"+str(round(circlespawns,1)),1, (105,0,102))
    screen.blit(label,(10, 10))
    circles=drawGradientBubble(circles)
    circlespawns+=circlespawnspeed+10000'''
    cx,cy,changex,changey,changez,cz=moveCharacter(cx,cy,changex,changey,changez,cz)
    if 1==mb[0]:
        for i in range(0,100):
            circles.append([mx,my,choice(choicelist),choice(choicelist),choice(choicelist),0])
    #draw.circle(screen,charactercolour,(int(cx),int(cy)),abs(int(cz/5)))
    ### END END END ###
    if len(circles)>2000:
        circles=circles[100:]
    draw.circle(screen,(255,255,255),(int(cx),int(cy)),2)
    print(clock.get_fps())
    display.flip()
quit()
