from pygame import gfxdraw
from pygame import mixer
from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1200,800)) #
running=True                        #
#####################################
font.init()
mixer.init()
font = font.SysFont("times new roman", 37)
mixer.music.load('1.mp3')
mixer.music.play()
mixer.music.set_volume(1)
def TitleScreen():
    running=True
    circles=[]
    choicelist=[i/1000 for i in range(-1000,1001)]
    choicelist2=[i/1000 for i in range(400,801)]
    choicelist3=[i/1000 for i in range(50)]
    choicelist4=[i/1000 for i in range(-3000,3001)]
    charactercolour=(0,0,0)
    
    newgametag=font.render('New Game', 1, (50,30,10))
    continuetag=font.render('Continue', 1, (50,30,10))
    optionstag=font.render('Options', 1, (50,30,10))
    exittag=font.render('Exit', 1, (50,30,10))
    buttons=[Rect(475,300,250,80),Rect(475,400,250,80),Rect(475,500,250,80),Rect(475,600,250,80)]
    def checkButtons(buttons,mx,my): #To go through the list of buttons and check if something collides with its Rect hitbox in the list
        for i in range(0,len(buttons)):
            if buttons[i].collidepoint(mx,my):
                gfxdraw.box(screen,buttons[i],(200,200,200,40))
    def drawMenu(): 
        drawalpharect(475,300,125,150,255)
        screen.blit(continuetag,(533,320))
        drawalpharect(475,400,125,150,255)
        screen.blit(newgametag,(515,420))
        drawalpharect(475,500,125,150,255)
        screen.blit(optionstag,(543,520))
        drawalpharect(475,600,125,150,255)
        screen.blit(exittag,(570,620))
        checkButtons(buttons,mx,my)
    def moveCharacter(cx,cy,changex,changey,changez,cz,acceleration,bouncex,bouncey):
        if 1==keys[119]:
            changey-=acceleration
        elif 1==keys[115]:
            changey+=acceleration
        if 1==keys[97]:
            changex-=acceleration
        elif 1==keys[100]:
            changex+=acceleration
        if cy+changey<0:
            changey=-changey*bouncey
        elif cy+changey>screen.get_height():
            changey=-changey*bouncey
        elif cx+changex<0:
            changex=-changex*bouncex
        elif cx+changex>screen.get_width():
            changex=-changex*bouncex
        if cz+changez>100:
            changez=-changez
        elif cz+changez<-100:
            changez=-changez
        cx+=changex
        cy+=changey
        cz+=changez
        return cx,cy,changex,changey,changez,cz
    clock=time.Clock()
    sx,sy=screen.get_width()//2,screen.get_height()//2
    while running:
        clock.tick(60)
        screen.fill((255,255,255))
        for evnt in event.get():
            if evnt.type == QUIT:
                running = False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
        keys=key.get_pressed()
        for i in range(0,1): #mx my changex changey changez z
            circles.append([sx,sy,choice(choicelist),choice(choicelist),choice(choicelist4),0,choice(choicelist3),choice(choicelist2),choice(choicelist2)])
        if len(circles)>3000:
            circles=circles[1:]
        for i in range(0,len(circles)):
            circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5]=moveCharacter(circles[i][0],circles[i][1],circles[i][2],circles[i][3],circles[i][4],circles[i][5],circles[i][6],circles[i][7],circles[i][8])
            draw.rect(screen,charactercolour,(int(circles[i][0]),int(circles[i][1]),abs(int(circles[i][5]/5)),abs(int(circles[i][5]/5))))
        drawMenu()
        display.flip()
    return
def checkButtons(buttons,mx,my): #To go through the list of buttons and check if something collides with its Rect hitbox in the list
    for i in range(0,len(buttons)):
        if buttons[i].collidepoint(mx,my):
            gfxdraw.box(screen,buttons[i],(200,200,200,40))
    return(buttons)
def drawalpharect(xx,yy,r,g,b):
    for x in range(0,25):
        gfxdraw.box(screen,(xx+x*2,yy+x,250-x*4,80-x*2),(r,g,b,x*5))
###
TitleScreen()
quit()
