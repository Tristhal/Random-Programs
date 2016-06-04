from pygame import *
from math import *
from random import *
#####################################
screen=display.set_mode((1200,900)) #
running=True                        #
#####################################
init()
lines=[]
distance="~"
cx,cy=(randint(0,screen.get_width()),randint(0,screen.get_height()))
bleh=image.load('Space.jpg')
space=image.load('Space.jpg')
space.set_alpha(50,SRCALPHA)
space2=space.copy()
space2.set_alpha(50,SRCALPHA)
#mouse.set_visible(False)
screen.blit(bleh,(0,0))
restart=0
x=60
mx,my=-500,-500
lowcase=0
highcase=50
for i in range(0,360,2):
        lenght=randint(0,50)
        changey=sin(radians(i))*x
        changex=cos(radians(i))*x
        changey1=sin(radians(i))*(x+lenght)
        changex1=cos(radians(i))*(x+lenght)
        lines.append([changex,changey,changex1,changey1])
def drawLines(lines,size):
    for i in lines:
        draw.line(space,(200,150,100),(mx+i[0],my+i[1]),(mx+i[2],my+i[3]),2)
myfont=font.SysFont("monospace", 20)
while running:
    clock=time.Clock()
    clock.tick(200)
    screen.blit(bleh,(0,0))
    screen.blit(space,(0,0))
    space=space2.copy()
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    if 1 in mb:
        screen.blit(space2,(0,0))
    for i in range(x,2,-1):
        draw.circle(space,(50+i*3,25+i*3,0+i*3),(mx,my),i)
    if ((mx-cx)**2+(my-cy)**2)**.5<=60:
        lowcase=(60-((mx-cx)**2+(my-cy)**2)**.5)*1.4
        highcase=(60-((mx-cx)**2+(my-cy)**2)**.5)*1.4+20
    else:
        lowcase,highcase=0,50
    if restart%2==0:
        lenght=randint(int(lowcase),int(highcase))
        changey=sin(radians(restart))*x
        changex=cos(radians(restart))*x
        changey1=sin(radians(restart))*(x+lenght)
        changex1=cos(radians(restart))*(x+lenght)
        lines[int(restart//2)]=[changex,changey,changex1,changey1]
        #draw.line(space,(255,255,255),(int(mx+changex),int(my+changey)),(int(mx+changex1),int(my+changey1)),2)
    drawLines(lines,2)
    #lines=[]
    if restart<358:
        restart+=2
    else:
        restart=0
    if 1 in mb:
        distance=str(((mx-cx)**2+(my-cy)**2)**.5)
    label=myfont.render("Distance: "+distance,1, (105,0,102))
    screen.blit(label,(10, 10))
    display.flip()
quit()
