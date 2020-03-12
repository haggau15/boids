from pygame import Vector2
import pygame

from drawobject import drawobject
class rectangle(drawobject):
    def __init__(self,color,x,y,height,width,sx):
        self.height=height
        self.width=width
        self.sx=sx
        super().__init__(color,x,y)

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))
    
    def move(self,screen_width, distance):
        if self.x+self.height+distance>screen_width or self.x+distance<40:
            return
        self.x+=distance

    def getrect(self):
            return pygame.Rect(self.x,self.y, self.height, self.width)
