from pygame import Vector2
import pygame

from rectangle import rectangle
#Strength is how many hits it can take before being removed
class block(rectangle):
        def __init__(self,color,x,y,height,width,strength):
            rectangle.__init__(self,color,x,y,height,width,0)
            self.strength = strength

        def draw(self,screen):
            pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))            

        def getrect(self):
            return (pygame.Rect)(self.x,self.y, self.height, self.width)

