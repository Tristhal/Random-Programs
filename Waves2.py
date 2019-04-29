# -*- coding: utf-8 -*-
#from scipy import *
from math import *
from pygame import *
from numpy import arctan
from pygame import gfxdraw

screenw = 1000
screenh = 600
mx2=0
my2=0   
############################################
screen=display.set_mode((screenw,screenh)) #
running=True                               #
############################################

class Node:
    def __init__(self, x, y, length, static, startnode = False):
        self.px = x
        self.py = y
        self.point = (x,y)
        self.vx = 0
        self.vy = 0
        self.k = 500
        self.mass = 100
        self.length = length
        self.parent = None
        self.child = None
        self.noderadius = 0
        self.forceconstant = 30.0
        self.forcex = 0.0
        self.forcey = 0.0
        self.startnode = startnode
        self.grabbed = False
        if(static):
            self.colour = (255,0,0)
            self.forceconstant = 100.0
            self.noderadius = 50
        else:
            self.colour = (255,255,255)
        self.static = static
    def drawNode(self, screen):
        if(self.child != None):
            #if(self.static == False):
            self.child.drawNode(screen)
            gfxdraw.aatrigon(screen, int(self.point[0]), int(self.point[1]),
                            int(self.child.point[0]), int(self.child.point[1]),
                            int(self.point[0]), int(self.point[1]), (255,255,255))
            self.child.drawNode(screen)
        #gfxdraw.aacircle(screen, int(self.px), int(self.py), self.noderadius, self.colour)
        #gfxdraw.filled_circle(screen, int(self.px), int(self.py), self.noderadius, self.colour)
    def checkMouse(self, mx, my, mb):
        if(mb[0] == 1 and (mx-self.px) != 0 and self.static == True):#check for division by zero and that the mouse is pressed
            if(((mx-self.px)**2 + (my-self.py)**2) <= self.noderadius**2):
            #if you are clicking on the node
                self.grabbed = True
                theta = atan((my-self.py)/(mx-self.px))
                if(mx < self.px):#To ensure the correct theta value 
                    self.py += sin(-theta)*2
                    self.px -= cos(-theta)*2
                else:
                    self.py += sin(theta)*2
                    self.px += cos(theta)*2
            elif(self.grabbed):
                theta = arctan((my-self.py)/(mx-self.px))
                if(mx < self.px):#To ensure the correct theta value 
                    self.py += sin(-theta)*2
                    self.px -= cos(-theta)*2#cos -theta is unchanged positive
                else:
                    self.py += sin(theta)*2
                    self.px += cos(theta)*2
        else:
            self.grabbed = False
        if(self.child != None):
            self.child.checkMouse(mx, my, mb)
    def updateForce(self, f1 = 0, f2 = 0):
        if(self.child != None and (self.child.px-self.px) != 0):
            theta = arctan((self.child.py-self.py)/(self.child.px-self.px))
            if(self.child.px < self.px):
                cmt = -1
            else:
                cmt = 1
            dist = sqrt((self.child.px-self.px)**2 + (self.child.py-self.py)**2) 
            fx, fy = (0,0)
            if(dist>self.length):
                dist -= self.length
                elasticforce = self.k*dist
                fx = (elasticforce)*cos(theta)
                fy = (elasticforce)*sin(theta*cmt)
                #if the child is to the right of this node
                if(self.child.px>self.px):
                    self.addForce(fx,0)
                    self.child.addForce(-fx,0)
                else:
                    self.addForce(-fx,0)
                    self.child.addForce(fx,0)
                #if the child is above this node
                if(self.child.py<self.py):
                    self.addForce(0,fy)
                    self.child.addForce(0,-fy)
                else:
                    self.addForce(0,fy)
                    self.child.addForce(0,-fy)
            elif(dist<self.length):
                dist = self.length-dist
                elasticforce = self.k*dist
                fx = (elasticforce)*cos(theta)
                fy = (elasticforce)*sin(theta*cmt)
                #if the child is to the right of this node
                if(self.child.px>self.px):
                    self.addForce(-fx,0)
                    self.child.addForce(fx,0)
                else:
                    self.addForce(fx,0)
                    self.child.addForce(-fx,0)
                #if the child is above this node
                if(self.child.py<self.py):
                    self.addForce(0,-fy)
                    self.child.addForce(0,fy)
                else:
                    self.addForce(0,-fy)
                    self.child.addForce(0,fy)
            if(dist > 4*self.length):
                self.vx*=.2
                self.vy*=.2
                self.forcex*=1
                self.forcey*=1
            self.child.updateForce(fx,fy)#continue updating force through the string
            #print(self.forcex,self.forcey)
            
        
    def updateNodeVelocity(self):
        if(self.static == False):
            self.vy = self.vy + self.forcey/self.mass*(.01) #v2 = v1 +at
            self.vy *= .9999
            self.vx = self.vx + self.forcex/self.mass*(.01) #v2 = v1 +at
            self.vx *= .9999
        if(self.child != None):
            self.child.updateNodeVelocity()
        self.forcex = 0
        self.forcey = 0
        
    def moveNode(self):
        self.py += self.vy
        self.px += self.vx
        if(self.child != None and self.child.child != None):
            pointx = (self.px+self.child.px+self.child.child.px)/(3)
            pointy = (self.py+self.child.py+self.child.child.py)/(3)
            self.point = (pointx,pointy)
        elif(self.child != None):
            pointx = (self.px+self.child.px)/(2)
            pointy = (self.py+self.child.py)/(2)
            self.point = (pointx,pointy)
        else:
            self.point = (self.px,self.py)
        if(self.child != None):
            self.child.moveNode()
    def addNode(self, node):
        if(self.child != None):
            self.child.addNode(node)
        else:
            self.setChild(node)
            self.child.setParent(self)
    def setChild(self, childnode):
        self.child = childnode
    def setParent(self, parentnode):
        self.parent = parentnode
    def addForce(self,forcex,forcey):
        self.forcex += forcex
        self.forcey += forcey
    def setStatic(self):
        self.static = True
        self.colour = (255,0,0)
        self.forceconstant = 100.0
        self.noderadius = 5
    def returnNode(self, pos, count = 0):
        if(count == pos):
            return self
        elif(self.child != None):
            return self.child.returnNode(pos, count+1)
        else:
            return self
    def addGravity(self, mag):
        self.addForce(0,mag*self.mass)
        if(self.child != None):
            self.child.addGravity(mag)
    def setMass(self,newmass):
        self.mass = newmass
###########################################################################################################################################################        
forceconstant = 10
nodespacing = 10
numnodes = 40
offsetx = -50
offsety = 100
startnode = Node(offsetx, offsety, nodespacing, False, True)
for i in range(1,numnodes):
    startnode.addNode(Node(offsetx+nodespacing*i+0*i, offsety, nodespacing, False, False))

startnode.returnNode(999).setStatic()
startnode.returnNode(0).setMass(1000)
#########################################################################################################################################################################################################################
 
while running:
    ###############################
    screen.fill((0,0,0))
    clock = time.Clock()
    clock.tick(100)
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys = key.get_pressed()
    changeX = (mx-mx2)
    changeY = (my-my2)
    ###############################
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    ###############################
    startnode.checkMouse(mx, my, mb)
    
    for i in range(10):
        startnode.addGravity(.1)
        startnode.updateForce()
        startnode.updateNodeVelocity()
        startnode.moveNode()
    startnode.drawNode(screen)
    
    
    ###############################
    if mx2!=mx:
        mx2=mx
    if my2!=my:
        my2=my
    display.flip()
    ###############################
quit()
    

    
