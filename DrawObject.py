from pygame import Vector2
import pygame

class DrawObject( object ):
    def __init__(self,color,x,y,height,width):
        self.y=y  
        self.x=x
        self.color=color
        self.height=height
        self.width=width

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))

    def get_middle_point(self):
        return (  self.x+(self.width/2),self.y+(self.height/2)  )




