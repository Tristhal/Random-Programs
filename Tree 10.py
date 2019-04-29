from pygame import *
from math import *
from random import *
import os
timee=260
#####################################
screen=display.set_mode((1000,800)) #
running=True                        #
#####################################
###
grass=image.load('grass.jpg')
fruit=[]
fruitspawn=[]
def grass(x,y,lenght,width,counter,colour):
    counter+=1
    width=lenght
    if counter==7:
        draw.rect(screen,(0,randint(colour-25,colour+25),0),(round(x),round(y),round(lenght/2),round(lenght/2)))
        draw.rect(screen,(0,randint(colour-25,colour+25),0),(round(x+lenght/2),round(y+lenght/2),round(lenght/2),round(lenght/2)))
        draw.rect(screen,(0,randint(colour-25,colour+25),0),(round(x+lenght/2),round(y),round(lenght/2),round(lenght/2)))
        draw.rect(screen,(0,randint(colour-25,colour+25),0),(round(x),round(y+lenght/2),round(lenght/2),round(lenght/2)))
        return
    grass(x,y,lenght/2,lenght/2,counter,colour)
    grass(x+lenght/2,y+width/2,lenght/2,lenght/2,counter,colour)
    grass(x+lenght/2,y,lenght/2,lenght/2,counter,colour)
    grass(x,y+width/2,lenght/2,lenght/2,counter,colour)
def treeDraw(startx,starty,lenght,branches,variantx,counter):
    variantxoriginal=variantx
    variant=randint(0,50)
    counter+=1
    for i in range(0,branches):
        variantx=variantxoriginal
        if i==2:
            variantx-=variant
            changey=sin(radians(270+variantx))*lenght
            changex=cos(radians(270+variantx))*lenght
            endx=startx+changex
            endy=starty+changey
        elif i==1:
            variantx+=variant
            changey=sin(radians(270+variantx))*lenght
            changex=cos(radians(270+variantx))*lenght
            endx=startx+changex
            endy=starty+changey
        elif i==0:
            #variantx-=15
            changey=sin(radians(270+variantx))*lenght
            changex=cos(radians(270+variantx))*lenght
            endx=startx+changex
            endy=starty+changey
        else:
            variant=randint(-30,30)
            variantx+=variant
            changey=sin(radians(270+variantx))*lenght
            changex=cos(radians(270+variantx))*lenght
            endx=startx+changex
            endy=starty+changey
        if counter>3:
            if randint(0,10)==3:
                return
        if lenght>1:
            draw.line(screen,(200,200,200),(startx,starty),(endx,endy))
            treeDraw(endx,endy,lenght//choice([1.3,1.7,2,1.3,1.7,2,1.3,1.7,2,.99,.99]),3,variantx,counter)
        else:
            '''for angle in range(0,361,40):
                changey=sin(radians(angle))*lenght
                changex=cos(radians(angle))*lenght
                endx=startx+changex
                endy=starty+changey'''
            draw.line(screen,(randint(0,255),randint(5,80),randint(5,90)),(startx,starty),(endx,endy))
            if randint(0,40)==1:
                fruitspawn.append([endx,endy])
            return
        display.update()
    return
grass(0,0,1000,800,0,timee//10)
screen2=screen.copy()
timeee=timee
lastcolour=(200,200,200)
##
while running:
    #screen.fill((0,0,0))
    screen.blit(screen2,(0,0))
    #grass(0,0,1000,800,0,timeee//10)
    clock=time.Clock()
    clock.tick(100)
    mx, my = mouse.get_pos()
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            treeDraw(mx,my,100,1,0,0)
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    #####################################################
    if timeee%10==0:
        screenpixel=PixelArray(screen)
        screenpixel.replace(lastcolour,(timeee/100,timeee/100,timeee/100))
        lastcolour=(timeee/100,timeee/100,timeee/100)
        screen2=screenpixel.make_surface()
        del screenpixel
    else:
        screen2=screen.copy()
    for i in range(len(fruit)-1,-1,-1):
        fruit[i][6]+=choice([1,2,.3,.4])
        if fruit[i][6]>2000:
            draw.circle(screen,(200,50,50),(int(fruit[i][0]),int(fruit[i][1])),fruit[i][3])
            if fruit[i][1]<screen.get_height()-20:
                if fruit[i][2]<=fruit[i][5]:
                    fruit[i][2]+=fruit[i][4]
                fruit[i][1]+=fruit[i][2]
        else:
            draw.rect(screen,(fruit[i][6]//10,50,0),(int(fruit[i][0]-fruit[i][3]),int(fruit[i][1]-fruit[i][3]),fruit[i][3]*2,fruit[i][3]*2))
    if randint(0,200)==1:
        currentfruit=choice(fruitspawn)
        currentfruitx,currentfruity=currentfruit[0],currentfruit[1]
        #endx,endy,acceleration,size,accelerationspeed,maxspeed,lifetimer
        fruit.append([currentfruitx,currentfruity,0,randint(2,6),choice([.0003,.0004,.0005,.0006,.0007,.00035,.00045,.00055,.00065,.00075]),choice([.3,.4,.5,.6,.7,.35,.45,.55,.65,.75]),0])
    if len(fruit)>500:
        del fruit[0]
    if timee>40590:
        timee=260
    if timee>21400:
        timeee=21500-(timee-21000)
    else:
        timeee=timee
    draw.circle(screen,(timeee/100,timeee/100,0),(100,100),60)
    timee+=10
    display.flip()
quit()
