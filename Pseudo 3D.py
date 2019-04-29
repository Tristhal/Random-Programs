from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1200,800)) #
running=True                        #
cx,cy,cz=400,300,0                  #
#####################################
acceleration=.05
changez=15
gravity=1.981
circles=[]
choicelist=[i/1000 for i in range(-1000,1001)]
choicelist2= choicelist.remove(0)
choicelist2=[1.5]
charactercolour=(0,0,0)
choicelist3=[i/1000 for i in range(-900,900)]
def moveCharacter(cx,cy,changex,changey,changez,cz,acceleration):
    if 1==keys[119]:
        changey-=acceleration
    if 1==keys[100]:
        changex+=acceleration
    if 1==keys[115]:
        changey+=acceleration
    elif 1==keys[97]:
        changex-=acceleration
    #changey+=gravity    
    if cy+changey<0:
        changey=-changey/choice(choicelist2)
    elif cy+changey>screen.get_height():
        changey=-changey/choice(choicelist2)
    elif cx+changex<0:
        changex=-changex/choice(choicelist2)
    elif cx+changex>screen.get_width():
        changex=-changex/choice(choicelist2)
    if cz+changez>100:
        changez=-changez
    elif cz+changez<-100:
        changez=-changez
        
    cx+=changex
    cy+=changey
    cz+=changez
    return cx,cy,changex,changey,changez,cz

clock=time.Clock()
while running:
    clock.tick(60)
    screen.fill((255,255,255))
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
    if 1==mb[0]:
        '''for blehx in range(0,300,20):
            for blehy in range(0,300,20):
                for i in range(0,1): #mx my changex changey changez z
                    circles.append([mx+blehx,my+blehy,0,0,0,100,choice(choicelist3)])'''
        for blehx in range(0,300,20):
            for i in range(0,1): #mx my changex changey changez z
                circles.append([mx+blehx,my,0,0,0,100,choice(choicelist3)])
        for blehx in range(0,301,20):
            for i in range(0,1): #mx my changex changey changez z
                circles.append([mx+blehx,my+300,0,0,0,100,choice(choicelist3)])
        for blehx in range(0,301,20):
            for i in range(0,1): #mx my changex changey changez z
                circles.append([mx,my+blehx,0,0,0,100,choice(choicelist3)])
        for blehx in range(0,300,20):
            for i in range(0,1): #mx my changex changey changez z
                circles.append([mx+300,my+blehx,0,0,0,100,choice(choicelist3)])
    if len(circles)>10000:
        circles=circles[100:]
    for i in range(0,len(circles)):
        circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5]=moveCharacter(circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5],circles[i][6])
        draw.rect(screen,charactercolour,(int(circles[i][0]),int(circles[i][1]),abs(int(circles[i][5]/5)),abs(int(circles[i][5]/5))))
    for x in circles:
        #for y in circles:
        y=choice(circles)
        #for y in circles:
       # draw.line(screen,(255,0,0),(int(x[0]),int(x[1])),(int(y[0]),int(y[1])))
    #print(clock.get_fps())
    display.flip()
quit()
