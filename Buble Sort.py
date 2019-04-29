from pygame import *
from random import *
screen=display.set_mode((1000,800))
running = True
clock=time.Clock()
mousestatus=[]
lines=[]
xes=[]
counter=0
nums = list(range(800))
shuffle(nums)
lines=list(range(800))
for x in range(0,800):
    lines[x]=nums[x]
while running:
    screen.fill((0,0,0))
    mousestatus=[]
    screen.fill((0,0,0))
    for evnt in event.get():
        if evnt.type==QUIT:
            running=False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    keys=key.get_pressed()
    #for bleaskjaskjhsafhksajhsfakhfaskjhfkhasfkjfaskfasjhs in range(0,100):
    for i in range(0,len(lines)):
        draw.line(screen,(255,255,255),(i,800),(i,lines[i]))
    for x in range(0,len(lines)-1):
        y,y2=lines[x],lines[x+1]
        blehx2=lines[x+1]
        blehx=lines[x]
        if y<y2:
            lines[x]=blehx2
            lines[x+1]=blehx
            counter+=1
    '''for x in range(len(lines)-2,-1,-1):
        y,y2=lines[x],lines[x+1]
        blehx2=lines[x+1]
        blehx=lines[x]
        if y<y2:
            lines[x]=blehx2
            lines[x+1]=blehx'''
    print(counter)
    display.flip()   
    clock.tick(10000)
quit()
