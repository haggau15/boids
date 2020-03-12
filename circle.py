from pygame import Vector2
import pygame
from physics import physics

from drawobject import drawobject
from rectangle import rectangle


#self,color,x,y,height,width
class circle(drawobject):
    def __init__(self,color,x,y,radius,hitbox,sx,sy):
        super().__init__(color,x,y)
        self.radius=radius
        self.sx=sx
        self.sy=sy
        self.hitbox=rectangle((0,0,100),self.x-self.radius,self.y-self.radius,self.radius*2,self.radius*2,self.sx)

    def move(self,hitsomething,s_height,s_width):
        
        #Checks if the ball has hit any objects
        if hitsomething==1:
            self.sy*=-1
        #Checks if the ball has hit the left side
        if self.x+self.radius>=s_width:
            self.sx*=-1
            self.x=s_width-self.radius
        #Checks if the ball has hit the right side
        if self.x-self.radius<=0:
            self.x=self.radius
            self.sx*=-1
        #Checks if the ball has hit the top
        if self.y-self.radius<=0:
            self.sy*=-1
        #Checks if the ball has hit the bottom
        if self.y+self.radius>=s_height:
            self.y=s_height-self.radius
            self.sy*=-1
            exit()
        self.x+=self.sx
        self.y+=self.sy

    def draw(self,screen):
        #Moves the htibox with the circle
        self.hitbox=rectangle((0,0,0),self.x-self.radius,self.y-self.radius,self.radius*2,self.radius*2,self.sx)
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    #Called when the ball hits the bat
    #The out angle from the bat is calculated based on how far from the middle the ball hit
    #The angle can be between 90 and 45 degrees
    def bat_hit(self,distfromcentre):
        if distfromcentre == 175:
            self.sx=0
            self.sy*=-1
            return
        elif distfromcentre < 175:
            i=int (175-distfromcentre)
            degrees=((i/175)*45)
            p = physics
            self.sx,self.sy = p.on_bat(10,degrees)
            self.sy*=-1
        elif distfromcentre > 175:
            i=int (distfromcentre/2)
            degrees=((i/175)*45)
            p = physics
            self.sx,self.sy = p.on_bat(10,degrees)
            self.sx*=-1
            self.sy*=-1
        

