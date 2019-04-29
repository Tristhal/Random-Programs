#graphics1.py
#Theme inspired by the Hoops and Yoyo characters
#Scroll wheel is used to be able to quickly place multiple images or string together shapes as well as increase
#line sizes. They all count as one image however to allow for more undo's.
##Hold right click and let go of left to undo a drawn line on the spot##
from pygame import *
from random import *
from math import *
import os
import glob
mx2,my2=0,0
mb2=(0,0,0)
stamp1=image.load(('rsz_stamp1.png'))
stamp2=image.load(('rsz_stamp2.png'))
stamp3=image.load(('rsz_stamp3.png'))
stamp4=image.load(('rsz_stamp4.png'))
stamp5=image.load(('rsz_stamp5.png'))
stamp6=image.load(('rsz_stamp6.png'))
buttons=[[Rect(849,99,42,42),0,"pencil",(850,100),image.load(('pencil.jpg'))],[Rect(899,99,42,42),0,"eraser",(900,100),image.load(('eraser.jpg'))],
         [Rect(949,99,42,42),0,"brush",(950,100),image.load(('brush.jpg'))],[Rect(849,149,42,42),0,"undo",(850,150),image.load(('undo.jpg'))],
         [Rect(899,149,42,42),0,"jaggedbrush",(900,150),image.load(('jagged brush.jpg'))],[Rect(949,149,42,42),0,"smoothbrush",(950,150),image.load(('smooth brush.jpg'))],
         [Rect(849,199,42,42),0,"rectfill",(850,200),image.load(('rect.jpg'))],[Rect(899,199,42,42),0,"rectunfill",(900,200),image.load(('unfilled rect.jpg'))],
         [Rect(949,199,42,42),0,"ellipsefill",(950,200),image.load(('circle.jpg'))],[Rect(849,249,42,42),0,"ellipseunfill",(850,250),image.load(('unfilled circle.jpg'))],
         [Rect(899,249,42,42),0,"save",(900,250),image.load(('save.jpg'))],[Rect(949,249,42,42),0,"load",(950,250),image.load(('load.jpg'))],
         [Rect(849,299,42,42),0,"line",(850,300),image.load(('line.jpg'))],[Rect(899,299,42,42),0,"spraycan",(900,300),image.load(('spray can.jpg'))],
         [Rect(949,299,42,42),0,"redo",(950,300),image.load(('redo.jpg'))],
         [Rect(39,691,102,102),0,"stamp1",(50,692),stamp1],
         [Rect(159,691,102,102),0,"stamp2",(160,692),stamp2],
         [Rect(269,691,102,102),0,"stamp3",(270,692),stamp3],
         [Rect(379,691,102,102),0,"stamp4",(380,692),stamp4],
         [Rect(489,691,102,102),0,"stamp5",(490,692),stamp5],
         [Rect(599,691,102,102),0,"stamp6",(600,692),stamp6]] #List of clickable buttons and their hit boxes.
#annoying things doodle and sketch can do
actions=[['pencil',"Yes yes the PENCIL is the best choice right now... Yes."],['undo',"SKETCH!!! WHOOPS. Thats undo... My bad!"],['stamp1',"You know you want some of me on there."],
         ['stamp2',"Um. HI! Yeah. You should place me here! PLS???"],['stamp6',"Thats bob... Or was that Jim, or Jum, or Joe, or maby Bob not bob..."],
         ['jaggedbrush',"Though unrefined like Sketch. This brush has character. YAY!!!"],['',"Wate just one second... What happened to your tool??? Hehehe."],
         ['brush',"Draw a starwhal for me please! I love that game."],['',"We have decided it is right to confiscate your tool. Yes."]]
copyscreen=False
undostatus=False
drewonscreen=False#to know if to copy screen
###
scrollup=False
scrolldown=False
filespos=0#for the scrolling menu for load
fileName=''
fileLoadName=''
returntool=False #when right-click-undoing this tells the undo to return to a tool after its done
doodlensketchtimer=0
colour=(0,0,0)#global colour
lineW=5#brush widths
jaggedbrushW=1
drawareapos=-1#preset widths for special brushes
smoothbrushW=5
mousestatus=''
selectedtool="pencil"
slope=0
slope2=0#used in smooth brush to calculate size change
###
screen=display.set_mode((1000,800))
screen.fill((0,0,0))
drawArea=Surface((800,600))#canvas
rect1=Surface((90,60))#transparent surfaces for looks
rect1.set_alpha(150,SRCALPHA)#thats why theyre called rect#
rect2=Surface((150,260))
rect2.set_alpha(100,SRCALPHA)
rect3=Surface((674,115))
rect3.set_alpha(100,SRCALPHA)
rect2.fill((240,240,255))
rect3.fill((240,240,255))
rect4=Surface((130,130))
rect4.set_alpha(200,SRCALPHA)
rect4.fill((255,255,255))
drawArea.fill((255,255,255))
drawareas=[drawArea.copy()]
chat='''Welcome... WELCOME!... sketch say welcome(forced whisper). WELCOME FORCED WHISPER!'''#beginning text and future text is stored here
###
colourpallet=image.load(('colour-pallet.png'))#background images
background=image.load(('cartoon-house-wide.jpg'))
logo=image.load(('Logo.png'))
doodle=image.load(('Doodle (2).png'))
sketch=image.load(('Sketch (2).png'))
font.init()#font preparing
font = font.SysFont("times new roman", 17) # Im using times new roman so its guarenteed the font is on the computerw
label=font.render(chat, 1, (50,30,10))     #not taking a risk here.
### Oh now i have to comment all these functions :(
def getText(text):#As the name sais. Using the key number as the chr code to convert the pressed input into a str
    for i in range(97,123):
        if keys[i]==1:
            text+=chr(i)
            break
    for i in range(49,58): #The numbers on the top row correspond to these numbers
        if keys[i]==1:
            text+=str(i-48)
    return text
def drawEllipse(mx,my,rectstartposx,rectstartposy,fill=True): #Taking the necesary inputs to draw the ellipse
    if fill==True:# Beating it to death with if statements to determin which quadrant the mouse is in
        mc,my=coordAdjust(mx,my) #and act accordingly.
        if mx-rectstartposx<=1 and my-rectstartposy>=1:
            draw.ellipse(drawArea,colour,(rectstartposx-abs(rectstartposx-mx),rectstartposy,abs(rectstartposx-mx),abs(rectstartposy-my)))
        elif mx-rectstartposx>=1 and my-rectstartposy<=1:
            draw.ellipse(drawArea,colour,(rectstartposx,rectstartposy-abs(rectstartposy-my),abs(rectstartposx-mx),abs(rectstartposy-my)))
        elif mx-rectstartposx<=1 and my-rectstartposy<=1:
            draw.ellipse(drawArea,colour,(rectstartposx-abs(rectstartposx-mx),rectstartposy-abs(rectstartposy-my),abs(rectstartposx-mx),abs(rectstartposy-my)))
        else:
            draw.ellipse(drawArea,colour,(rectstartposx,rectstartposy,mx-rectstartposx,my-rectstartposy))
    else:
        try:
            mc,my=coordAdjust(mx,my)
            if mx-rectstartposx<=1 and my-rectstartposy>=1:
                draw.ellipse(drawArea,colour,(rectstartposx-abs(rectstartposx-mx),rectstartposy,abs(rectstartposx-mx),abs(rectstartposy-my)),1)
            elif mx-rectstartposx>=1 and my-rectstartposy<=1:
                draw.ellipse(drawArea,colour,(rectstartposx,rectstartposy-abs(rectstartposy-my),abs(rectstartposx-mx),abs(rectstartposy-my)),1)
            elif mx-rectstartposx<=1 and my-rectstartposy<=1:
                draw.ellipse(drawArea,colour,(rectstartposx-abs(rectstartposx-mx),rectstartposy-abs(rectstartposy-my),abs(rectstartposx-mx),abs(rectstartposy-my)),1)
            else:
                draw.ellipse(drawArea,colour,(rectstartposx,rectstartposy,mx-rectstartposx,my-rectstartposy),1)
        except:
            pass
def DOODLEnSKETCH(): # This is to add some flavour to the paint. The mascots will change your tool every so often
    global selectedtool   #to spice up the experience.
    global chat
    global label
    currentaction=choice(actions)
    selectedtool=currentaction[0]
    label=font.render(currentaction[1],0,(50,30,10))
def drawCollide(mx,my): #Checks collisions with the screen using coordinants for the drawing surface
    mx,my=coordReturn(mx,my)
    return Rect(40,80,800,600).collidepoint(mx,my)
def getColour(mx,my,colour): #An ease of life function to speed things up later
    if  Rect(40,80,800,600).collidepoint(mx,my)==False:
        colour=screen.get_at((mx,my))
    return colour
def coordAdjust(mx,my):# I use this to try to minimize the hard coded numbers. 
    return mx-40,my-80 # though for some reason i cant use the output in functions with (something,something) so i have some disclamers later.
def coordReturn(mx,my):# Reverse of above.
    return mx+40,my+80
def drawLine(mx,my,mx2,my2,colour):#Takes previous mouse coords and draws a line with the current colour.
    global drewonscreen
    mx,my=coordAdjust(mx,my)
    mx2,my2=coordAdjust(mx2,my2)
    draw.aaline(drawArea,colour,(mx2,my2),(mx,my))
    changeX=(mx-mx2)
    changeY=(my-my2)
    if (mx,my)!=(mx2,my2):
        for i in range(1,int((changeX**2+changeY**2)**.5)):
            xCoords=mx2+(i*(changeX))/int((changeX**2+changeY**2))**.5
            yCoords=my2+(i*(changeY))/int((changeX**2+changeY**2))**.5
            if drawCollide(mx,my)==True:
                drewonscreen=True
                break
def thickLine(mx,my,mx2,my2,colour,radius): #uses the formula to cut up a line between two points
    global drewonscreen                     #to draw a line of circles with colours colour and lineW as radius
    mx,my=coordAdjust(mx,my)
    mx2,my2=coordAdjust(mx2,my2)
    changeX=(mx-mx2)
    changeY=(my-my2)
    if (mx,my)!=(mx2,my2):
        for i in range(1,int((changeX**2+changeY**2)**.5)):
            xCoords=mx2+(i*(changeX))/int((changeX**2+changeY**2))**.5
            yCoords=my2+(i*(changeY))/int((changeX**2+changeY**2))**.5
            if drawCollide(mx,my)==True:# if any circle is drawn on the screen it needs to be recorded for the undo to occur
                draw.circle(drawArea,colour,(int(xCoords),int(yCoords)),radius)# I use this for all the lines
                drewonscreen=True
            else:
                break
    else:
        draw.circle(drawArea,colour,(mx,my),radius)
def jaggedBrush(mx,my,mx2,my2,colour):#makes a brush with an interesting look by drawing lines and circles of different
    global drewonscreen #sizes based on your mouse movement speed
    mx,my=coordAdjust(mx,my)
    mx2,my2=coordAdjust(mx2,my2)
    jaggedbrushW=abs(mx2-mx+my2-my)/2
    if jaggedbrushW<4:
        jaggedbrushW=4
    draw.line(drawArea,colour,(mx2,my2),(mx,my),int(jaggedbrushW))
    if jaggedbrushW//2-2>1:
        draw.circle(drawArea,colour,(mx,my),int(jaggedbrushW//2-2))
    if drawCollide(mx,my)==True:
                drewonscreen=True
def smoothBrush(mx,my,mx2,my2,slope,slope2,smoothbrushW,colour):# simiar to jagged brush only smooth
    global drewonscreen
    changeX=(mx-mx2)#changes the size incrementally each time when the change in slopes is beyond a certain threshold
    changeY=(my-my2)
    mx,my=coordAdjust(mx,my)
    mx2,my2=coordAdjust(mx2,my2)
    if changeX!=0 and changeY!=0:
        slope=changeY/changeX
    if smoothbrushW<15 and abs(slope-slope2)>.5:
        smoothbrushW+=1.5
    else:
        if smoothbrushW>=6 and abs(slope-slope2)!=0:
            smoothbrushW-=1.5
    for i in range(1,int((changeX**2+changeY**2)**.5)):
        xCoords=mx2+(i*(changeX))/int((changeX**2+changeY**2))**.5
        yCoords=my2+(i*(changeY))/int((changeX**2+changeY**2))**.5
        draw.circle(drawArea,colour,(int(xCoords),int(yCoords)),int(smoothbrushW/2))
        if drawCollide(mx,my)==True:
                drewonscreen=True
                
    return slope,slope2,smoothbrushW
def erase(mx,my,mx2,my2,radius): # calls thickline with a white colour Could be modified to be background specific
    thickLine(mx,my,mx2,my2,(255,255,255),radius) 
def checkButtons(mx,my,buttons): #To go through the list of buttons and check if something collides with its Rect hitbox in the list
    global selectedtool # of buttons
    global lineW
    global colour #Sorry about all the globals i know they are bad but for the purpose of some functs it easier with them
    for i in range(0,len(buttons)):
        if buttons[i][0].collidepoint(mx,my):
            selectedtool=buttons[i][2]
            lineW=5
    return(buttons)
def drawButtons(buttons):# Given information from the list of buttons it draws them at their specified coordinants
    for i in range(0,len(buttons)):
        if buttons[i][2]==selectedtool:
            draw.rect(screen,(0,0,0),buttons[i][0])
            screen.blit(buttons[i][4],buttons[i][3])
        else:
            screen.blit(buttons[i][4],buttons[i][3])
    return(buttons)
def drawTool(mousestatus):# a function as something of a backup to say something was drawn if the mouse ends on the
    global copyscreen #draw area
    global drewonscreen
    copyscreen=True #sais to copy the screen
    if mousestatus=="UP" and drawCollide(mx-40,my-80): #Tip for me: !!!!!!!!!!If you move screen update coord adjust!!!!!!!!!
        drewonscreen=True
    return(drawArea.copy()) #a copy of the canvas is made
        
running=True
###
screen.blit(background,(0,0)) #background #background
screen.blit(logo,(350,20))
rect1.fill((255,255,255))
screen.blit(rect1,(890,5))
screen.blit(doodle,(900,25))
screen.blit(sketch,(930,30))
###
display.set_caption("DnS Paint","DnS Paint")#title name
while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0)) #background #background
    screen.blit(colourpallet,(650,550))
    for i in range(-20,63): #makes fancy black gradient WOO
        draw.circle(screen,(abs(i*4),abs(i*4),abs(i*4)),(970,580),63-i)
    screen.blit(logo,(350,20))#blitting all the fancy screen graphics
    screen.blit(rect1,(890,22))#transparent piece
    draw.rect(screen,(0,0,0),(889,21,92,62),1)
    screen.blit(doodle,(900,25))#mascots
    screen.blit(sketch,(930,30))
    draw.rect(screen,(0,0,0),(38,78,803,603),2) #frame
    draw.rect(screen,(0,0,0),(0,0,1000,800),1) #frame
    #draw.rect(screen,(240,240,255),(845,90,150,260))
    screen.blit(rect2,(845,90))
    draw.rect(screen,(0,0,0),(843,88,154,264),2)
    #draw.rect(screen,(240,240,255),(34,686,670,111))
    screen.blit(rect3,(34,686))
    draw.rect(screen,(0,0,0),(32,683,675,116),2)
    drawButtons(buttons) #buttons
#############################################################################################################################################################################################################################################
    clock=time.Clock()
    clock.tick(100000)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
#############################################################################################################################################################################################################################################
    screen.blit(drawArea,(40,80)) #Draws canvas
    rect4.fill((255,255,255))
    draw.circle(rect4,colour,(65,65),60,2) #Draw the size and colour display
    draw.circle(rect4,colour,(65,65),lineW) #The order is used to determine which is ontop
    screen.blit(rect4,(855,360))
    draw.rect(screen,(0,0,0),(853,358,133,133),2)
    for evnt in event.get():
        if evnt.type==MOUSEBUTTONDOWN:
            if evnt.button==4:#change line sizes with scroll
                if lineW>4:
                    lineW-=2
                scrolldown=True
            if evnt.button==5:
                if lineW+2<60: #brush size cap
                    lineW+=2
                scrollup=True
            if evnt.button==1:
                buttons=checkButtons(mx,my,buttons) #checks for the pressed buttons. Placement logic being if the mouse was pressed
            mousestatus="DOWN"
            if evnt.button==3:
                colour=getColour(mx,my,colour) #picks the colour anywhere on the screen because the background has some very nice colours(I did actually intend to do this flavour)
        elif evnt.type==MOUSEBUTTONUP:
            if mb[2]==1 and evnt.button==1 and selectedtool in ['pencil','eraser','jaggedbrush','smoothbrush','brush']:
                returntool=selectedtool
                selectedtool='undo'
                drawArea=(drawareas[drawareapos]).copy()
                #mousestatus='UP'
            else:
                returntool=False      
        elif evnt.type==KEYDOWN:
            keydown=True
        elif evnt.type == QUIT:
            running = False
    if mb[0]==0 and mb2[0]==1: #checks to see if the mouse button was released (event loop didn't work for some reason for up)
        mousestatus="UP"
#############################################################################################################################################################################################################################################            
    #AAND the longist if statement I have ever made
    ####The general idea is if any pencil is selected something is drawn becomes true so you dont get funky undoing(it cuts of the end of the undo
        #list.append) and to perform the tasks required by each tool.
        #The undo is out of the if statment because i dont want to mess with that because I believe there is a case where it messes up if it is.
        #The code generally dosent need a function but to try to reduce the size of the while running loop i made them functions.
    if selectedtool=="pencil": #If pencil tool is selected
        if mb[0]==1: 
            drawLine(mx,my,mx2,my2,colour) #Function draws aaline
        drewsomething=True #something has been drawn
        if mousestatus=="UP": #copies the
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="spraycan":
        if mb[0]==1:
            for i in range(0,lineW):
                draw.circle(screen,(0,0,0),(mx,my),lineW+1,1)
                angle=radians(randint(0,360))# sets hypotenuse lenght a set number and allows for it to change
                lenght=randint(-lineW,lineW)
                changex=sin(angle)*lenght
                changey=cos(angle)*lenght
                draw.circle(drawArea,colour,(coordAdjust(int(mx+changex),int(my+changey))),0)
        drewsomething=True #something has been drawn
        if mousestatus=="UP": #copies the
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="eraser":
        if 1==mb[0]:
            draw.circle(screen,(0,0,0),(mx,my),lineW,1)
            erase(mx,my,mx2,my2,lineW)
        drewsomething=True
        if mousestatus=="UP":
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="brush":
        if 1==mb[0]:
            thickLine(mx,my,mx2,my2,colour,lineW)
        drewsomething=True
        if mousestatus=="UP":
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="jaggedbrush":
        if 1==mb[0]:
            jaggedBrush(mx,my,mx2,my2,colour)
        drewsomething=True
        if mousestatus=="UP":
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="smoothbrush":
        if 1==mb[0]:
            slope,slope2,smoothbrushW=smoothBrush(mx,my,mx2,my2,slope,slope2,smoothbrushW,colour)
        drewsomething=True
        if mousestatus=="UP":
            tempscreen=drawTool(mousestatus)
    elif selectedtool=="rectfill": #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy() # For all the shape tools its essentially the same code just drawing
        if mousestatus=="DOWN":      #another shape.
            startcanvas=drawArea.copy()#canvas copy to revert to
            rectstartposx,rectstartposy=coordAdjust(mx,my) #sets the starting positions of the shape
            if drawCollide(mx-40,my-80):#If the shape started on the screen then somethings been drawn: Here i wanted to use the coordAdjust() but
                drewonscreen=True#it did not work even thought the function returned something,something and you can do x,x=coordAdjust(x,x)
        if mb[0]==1:
            drawArea=startcanvas.copy()#Before displaying the new 'fake' rectangle the screen has to be reverted so you dont get a giant blob of rects
            draw.rect(drawArea,colour,(rectstartposx,rectstartposy,mx-40-rectstartposx,my-80-rectstartposy))
        if mousestatus=="UP":
            drawArea=startcanvas.copy()#once again the screen must be cleared otherwise there is actually 2 rects remaining on the screen and can sometimes appear weird without.
            draw.rect(drawArea,colour,(rectstartposx,rectstartposy,mx-40-rectstartposx,my-80-rectstartposy))# coords adjusted to fit on the draw area
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    elif selectedtool=="rectunfill": #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy()
        if mousestatus=="DOWN":
            startcanvas=drawArea.copy()
            rectstartposx,rectstartposy=coordAdjust(mx,my)
            if drawCollide(mx-40,my-80):
                drewonscreen=True
        if mb[0]==1:
            drawArea=startcanvas.copy()
            draw.rect(drawArea,colour,(rectstartposx,rectstartposy,mx-40-rectstartposx,my-80-rectstartposy),1)
        if mousestatus=="UP":
            drawArea=startcanvas.copy()
            draw.rect(drawArea,colour,(rectstartposx,rectstartposy,mx-40-rectstartposx,my-80-rectstartposy),1)#!!!coords adjusted to fit on the draw area!!!
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    elif selectedtool=="ellipsefill": #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy()
        if mousestatus=="DOWN":
            startcanvas=drawArea.copy()
            rectstartposx,rectstartposy=coordAdjust(mx,my)
            if drawCollide(mx-40,my-80):
                drewonscreen=True
        if mb[0]==1:
            drawArea=startcanvas.copy()
            drawEllipse(mx,my,rectstartposx,rectstartposy)
        if mousestatus=="UP":
            drawArea=startcanvas.copy()
            drawEllipse(mx,my,rectstartposx,rectstartposy)
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    elif selectedtool=="ellipseunfill": #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy()
        if mousestatus=="DOWN":
            startcanvas=drawArea.copy()
            rectstartposx,rectstartposy=coordAdjust(mx,my)
            if drawCollide(mx-40,my-80):
                drewonscreen=True
        if mb[0]==1:
            drawArea=startcanvas.copy()
            drawEllipse(mx,my,rectstartposx,rectstartposy,False)
        if mousestatus=="UP":
            drawArea=startcanvas.copy()
            drawEllipse(mx,my,rectstartposx,rectstartposy,False)
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    elif selectedtool=="line": #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy()
        if mousestatus=="DOWN":
            startcanvas=drawArea.copy()
            rectstartposx,rectstartposy=coordAdjust(mx,my)
            if drawCollide(mx-40,my-80):
                drewonscreen=True
        if mb[0]==1:
            drawArea=startcanvas.copy()
            draw.line(drawArea,colour,(rectstartposx,rectstartposy),(coordAdjust(mx,my)),1)
        if mousestatus=="UP":
            drawArea=startcanvas.copy()
            draw.line(drawArea,colour,(rectstartposx,rectstartposy),(coordAdjust(mx,my)),1)
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    elif 'stamp' in selectedtool: #Tip for me: !!!!!!!!!Change the cord adjustments manually if you move the screen!!!!!!!!!!
        drawareacopy=drawArea.copy() #same code as above just changing it to images
        if mousestatus=="DOWN":
            startcanvas=drawArea.copy()
            if drawCollide(mx-40,my-80):
                drewonscreen=True
        if mb[0]==1:
            drawArea=startcanvas.copy()
            if selectedtool=='stamp1': #if statement inside of the stamp elif to reduce lag
                drawArea.blit(stamp1,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp2':
                drawArea.blit(stamp2,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp3':
                drawArea.blit(stamp3,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp4':
                drawArea.blit(stamp4,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp5':
                drawArea.blit(stamp5,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp6':
                drawArea.blit(stamp6,(coordAdjust(mx-50,my-50)))
        if mousestatus=="UP":
            drawArea=startcanvas.copy()
            if selectedtool=='stamp1': #if statement inside of the stamp elif to reduce lag
                drawArea.blit(stamp1,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp2':
                drawArea.blit(stamp2,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp3':
                drawArea.blit(stamp3,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp4':
                drawArea.blit(stamp4,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp5':
                drawArea.blit(stamp5,(coordAdjust(mx-50,my-50)))
            elif selectedtool=='stamp6':
                drawArea.blit(stamp6,(coordAdjust(mx-50,my-50)))
            tempscreen=drawTool(mousestatus)
            drewsomething=True
    if selectedtool=="undo":
        if abs(drawareapos)<len(drawareas):
            if mousestatus=="UP": #When the click finishes
                if abs(drawareapos)<=len(drawareas): #the screen to be copied
                    drawareapos-=1
                if abs(drawareapos)<=len(drawareas):
                    drawArea=(drawareas[drawareapos]).copy()
                undostatus=True
        if returntool!=False:
            selectedtool=returntool
    if copyscreen==True and drewonscreen==True:
        drewonscreen=False
        if len(drawareas)>20: #Caps undo depth to 20 screens
            drawareas=drawareas[1:]
        if drewsomething==True and undostatus==True: #if you draw again after undoing 
            undostatus=False
            drawareas=drawareas[0:drawareapos+1]#it cuts off everything after the screen your at
            drawareapos=-1 #sets the position to the end again
        drawareas.append(tempscreen) #appens the copy of the screen (tempscreen) if needed
    if selectedtool=="save":
        keys=key.get_pressed()
        if keydown==True and len(fileName)<24:
            fileName=getText(fileName)
            if keys[8]==1:
                fileName=fileName[:-1]
        if keys[13]==1:
            selectedtool="pencil"
            image.save(drawArea,os.path.join('screenshots',fileName+'.jpg'))
            fileName=""
        draw.rect(screen,(255,255,255),(49,50,220,25))
        draw.rect(screen,(0,0,0),(48,49,222,27),1)
        screen.blit(font.render(fileName+'.jpg',1,(0,0,0)),(50,50))
    elif selectedtool=="load":
        keys=key.get_pressed()#updates key status as its placed before the event loop
        if keydown==True and len(fileLoadName)<24:
            fileLoadName=getText(fileLoadName)#adds to the file name so long as its not past the letter cap
        if keydown==True:
            if keys[8]==1:
                fileLoadName=fileLoadName[:-1]#backspace to remove the last chr
        if keys[13]==1:
            selectedtool="pencil"
            try:
                drawArea=image.load(os.path.join('Screenshots\\'+fileLoadName+'.jpg'))#switches the canvas to the other image
            except:
                pass
            fileLoadName=''
        files=glob.glob(os.path.join('Screenshots\*'))
        if scrollup==True and filespos-1>=0:
            filespos-=1
        elif scrolldown==True and abs(filespos+1)<len(files):
            filespos+=1
        draw.rect(screen,(255,255,255),(49,50,220,25))
        draw.rect(screen,(0,0,0),(48,49,222,27),1)
        screen.blit(font.render(fileLoadName,1,(0,0,0)),(50,50))
        draw.rect(screen,(255,255,255),(49,100,320,25))
        draw.rect(screen,(0,0,0),(48,99,322,27),1)
        screen.blit(font.render(files[filespos],1,(0,0,0)),(50,100))
    copyscreen=False #copy screen isn't true
    scrollup=False
    scrolldown=False
    drewsomething=False #nothing has been drawn
    mb2=mb #previous  mouse information
    if mx2!=mx:
        mx2=mx
    if my2!=my:
        my2=my
    if (slope-slope2)!=0: #slope of the line between mouse pos's
        slope2=slope
    mousestatus="none"
    keydown=False
    if randint(0,10000)==2355:
        label=font.render('Some dots here some dots there',1,(0,0,0))
        for i in range(0,10):
              draw.circle(drawArea,(randint(0,255),randint(0,255),randint(0,255)),(randint(0,1000),randint(0,800)),randint(10,300))
    if randint(0,3000)==1124:#just make this false if you want to disable for testing purposes
        DOODLEnSKETCH()# Doodle and Sketch mess with your program here switching tools with some flavour text
    screen.blit(label,(0,0))
    display.flip() #bleh
quit()
#The code is so short. It makes me feel like im missing something fundamental. I really dont know if this is considered messy code. I did not go back
#and reread already written code as long as it worked so im not sure how easy it is to understand. I tried to put comments to show my thinking
#but my thinking does seem weird and contorted when I look back. I hope it's not too ugly.
