from pygame import Vector2
import pygame
import random
from Boid import Boid
from MoveObject import MoveObject
from DrawObject import DrawObject
red=(255,25,25)
blue=(25,25,255)        
green=(25,255,25)

class InitObjects():
    def __init__(self,screen_x,screen_y):
        self.screen_x=screen_x
        self.screen_y=screen_y

    def GetBoids(self):
        size=25
        boids=[]
        for i in range(30):
            boids.append(MoveObject(green,self.rndint(0+100,self.screen_x-size-100),self.rndint(100,self.screen_y-size-100),size,size,self.rndint(-3,3),self.rndint(-3,3)))

        return boids

    def GetHoiks(self):
        size=50
        hoiks=[]
        for i in range(5):
            hoiks.append(MoveObject(red,self.rndint(0,self.screen_x-size),self.rndint(0,self.screen_y-size),size,size,self.rndint(-3,3),self.rndint(-3,3)))

        return hoiks

    def GetObstacles(self):
        size=75
        obstacles=[]
        for i in range(4):
            obstacles.append(DrawObject(blue,self.rndint(size,self.screen_x-size),self.rndint(size,self.screen_y-size),75,75))

        return obstacles
    
    def rndint(self,min,max):
        i=random.randint(min,max)
        if i==0:
            return 1
        return i
    