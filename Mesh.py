# -*- coding: utf-8 -*-
from scipy import *
from pygame import *
from pygame import gfxdraw
screenw = 1500
screenh = 800
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
        self.vx = 0
        self.vy = 0
        self.k = 500
        self.mass = 100
        self.length = length
        self.parent = []
        self.child = []
        self.noderadius = 0
        self.forceconstant = 30.0
        self.forcex = 0.0
        self.forcey = 0.0
        self.startnode = startnode
        self.grabbed = False
        if(static):
            self.colour = (255,0,0)
            self.forceconstant = 100.0
            self.noderadius = 5
        else:
            self.colour = (255,255,255)
        self.static = static
    def drawNode(self, screen):
        if(len(self.child) != 0):
            for child in self.child:
                gfxdraw.aatrigon(screen, int(round(self.px)), int(round(self.py)),
                             int(round(child.px)), int(round(child.py)),int(round(self.px)), int(round(self.py)), (255,255,255))
            self.child[0].drawNode(screen)
        gfxdraw.aacircle(screen, int(self.px), int(self.py), self.noderadius, self.colour)
        gfxdraw.filled_circle(screen, int(self.px), int(self.py), self.noderadius, self.colour)
    def checkMouse(self, mx, my, mb):
        if(mb[0] == 1 and (mx-self.px) != 0 and self.static == True):#check for division by zero and that the mouse is pressed
            if(((mx-self.px)**2 + (my-self.py)**2) <= self.noderadius**2):
            #if you are clicking on the node
                self.grabbed = True
                theta = arctan((my-self.py)/(mx-self.px))
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
        if(len(self.child) != 0):
            self.child[0].checkMouse(mx, my, mb)
    def updateForce(self, f1 = 0, f2 = 0):
        for child in self.child:
            if((child.px-self.px) != 0):
                theta = arctan((child.py-self.py)/(child.px-self.px))
                if(child.px < self.px):
                    cmt = -1
                else:
                    cmt = 1
                dist = sqrt((child.px-self.px)**2 + (child.py-self.py)**2) 
                fx, fy = (0,0)
                if(dist>self.length):
                    dist -= self.length
                    elasticforce = self.k*dist
                    fx = (elasticforce)*cos(theta)
                    fy = (elasticforce)*sin(theta*cmt)
                    #if the child is to the right of this node
                    if(child.px>self.px):
                        self.addForce(fx,0)
                        child.addForce(-fx,0)
                    else:
                        self.addForce(-fx,0)
                        child.addForce(fx,0)
                    #if the child is above this node
                    if(child.py<self.py):
                        self.addForce(0,fy)
                        child.addForce(0,-fy)
                    else:
                        self.addForce(0,fy)
                        child.addForce(0,-fy)
                elif(dist<self.length):
                    dist = self.length-dist
                    elasticforce = self.k*dist
                    fx = (elasticforce)*cos(theta)
                    fy = (elasticforce)*sin(theta*cmt)
                    #if the child is to the right of this node
                    if(child.px>self.px):
                        self.addForce(-fx,0)
                        child.addForce(fx,0)
                    else:
                        self.addForce(fx,0)
                        child.addForce(-fx,0)
                    #if the child is above this node
                    if(child.py<self.py):
                        self.addForce(0,-fy)
                        child.addForce(0,fy)
                    else:
                        self.addForce(0,-fy)
                        child.addForce(0,fy)
                '''if(dist > 1.5*self.length):
                    if(self.py-child.py > 0):#below
                        if(self.vx > 0):#moving down
                            self.vx*=-.5
                        else:
                            pass
                    else:
                        if(self.vx < 0):#moving up
                            self.vx*=-.5
                        else:
                            pass
                    #self.forcex*=.5
                    #self.forcey*=.5'''
        if(len(self.child) != 0):
            self.child[0].updateForce()#continue updating force through the string
            #print(self.forcex,self.forcey)
            
        
    def updateNodeVelocity(self):
        if(self.static == False):
            self.vy = self.vy + self.forcey/self.mass*(.01) #v2 = v1 +at
            self.vy *= .99
            self.vx = self.vx + self.forcex/self.mass*(.01) #v2 = v1 +at
            self.vx *= .99
        if(len(self.child) != 0):
            self.child[0].updateNodeVelocity()
        self.forcex = 0
        self.forcey = 0
        
    def moveNode(self):
        
        self.py += self.vy
        self.px += self.vx
        if(len(self.child) != 0):
            self.child[0].moveNode()
    def addNode(self, node):
        if(len(self.child) != 0):
            self.child[0].addNode(node)
        else:
            self.addChild(node)
            node.addParent(self)
    def addChild(self, childnode):
        self.child.append(childnode)
    def addParent(self, parentnode):
        self.parent.append(parentnode)
    def addForce(self,forcex,forcey):
        self.forcex += forcex
        self.forcey += forcey
    def setStatic(self):
        self.static = True
        self.colour = (255,0,0)
        self.forceconstant = 100.0
        self.noderadius = 5
    def returnNode(self, pos, count = 0):#only works for strings
        if(count == pos):
            return self
        elif(len(self.child) != 0):
            return self.child[0].returnNode(pos, count+1)
        else:
            return self
    def addGravity(self, mag):
        if(len(self.child) != 0):
            self.child[0].addGravity(mag)
        self.forcey += mag*self.mass
                
###########################################################################################################################################################        
gravity = 2
nodespacing = 50
startnodes = []
strands = 5
numnodes = 25
offsetx = 10
offsety = 10
for i in range(strands):
    startnodes.append(Node(offsetx, offsety+nodespacing*i, nodespacing, False, True))
for x in range(strands):
    for i in range(1,numnodes):
        startnodes[x].addNode(Node(offsetx+nodespacing*i+2*i, offsety+nodespacing*x, nodespacing, False, True))
startnodes[0].returnNode(0).setStatic()
startnodes[0].returnNode(9099).setStatic()
#startnodes[0].returnNode(numnodes/2).setStatic()
#startnodes[strands-1].returnNode(0).setStatic()
#startnodes[strands-1].returnNode(999999).setStatic()
'''for i in range(1,len(startnodes)):
    for j in range(40):
        startnodes[i].returnNode(j).addChild(startnodes[i-1].returnNode(j))'''
for i in range(0,len(startnodes)-1):
    for j in range(numnodes):
        startnodes[i].returnNode(j).addChild(startnodes[i+1].returnNode(j))
for i in range(0,len(startnodes)-1):
    for j in range(numnodes-1):
        startnodes[i].returnNode(j).addChild(startnodes[i+1].returnNode(j+1))
'''for i in range(0,len(startnodes)-1):
    for j in range(numnodes-1):
        startnodes[i].returnNode(j).addChild(startnodes[i+1].returnNode(j+1))'''

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
    
    for nodes in startnodes:
        nodes.checkMouse(mx, my, mb)
    for i in range(1):
        for nodes in startnodes:
            nodes.addGravity(gravity)
        #for nodes in startnodes:    
            #startnodes[1].addGravity(10)
            nodes.updateForce()
        #for nodes in startnodes:    
            #startnodes[1].updateForce()
            nodes.updateNodeVelocity()
        #for nodes in startnodes:    
            #startnodes[1].updateNodeVelocity()
            nodes.moveNode()
            #startnodes[1].moveNode()
    for nodes in startnodes:
        nodes.drawNode(screen)
    
    
    ###############################
    if mx2!=mx:
        mx2=mx
    if my2!=my:
        my2=my
    display.flip()
    ###############################
quit()
    

    
