from pygame import Vector2
import pygame
from MoveObject import MoveObject

class Hoik( MoveObject ):
    def __init__(self,color,x,y,height,width):
        super().__init__(color,x,y,height,width)
