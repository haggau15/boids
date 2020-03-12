from pygame import Vector2
import pygame
from MoveObject import MoveObject

class Boid( MoveObject ):
    def __init__(self,color,x,y,height,width,sx,sy):
        super().__init__(color,x,y,height,width,sx,sy)
    
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.height,self.width))