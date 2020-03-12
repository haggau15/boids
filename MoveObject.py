from pygame import Vector2
import pygame
from DrawObject import DrawObject

class MoveObject( DrawObject ):
    def __init__(self,color,x,y,height,width,sx,sy):
        super().__init__(color,x,y,height,width)
        self.sx=sx
        self.sy=sy

    def draw(self,screen):
        self.x+=self.sx
        self.y+=self.sy
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))

    def get_speed(self):
        return Vector2(self.sx,self.sy)