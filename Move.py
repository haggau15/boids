from pygame import Vector2
import pygame
from Boid import Boid
from MoveObject import MoveObject
import math

class Move():
    def __init__(self,screen_x,screen_y):
        self.screen_x=screen_x
        self.screen_y=screen_y

    #Returns average position of nearby boids
    def get_average_pos(self,nearby_boids):
        y=1
        x=1
        for boid in nearby_boids:
            y+=boid.y
            x+=boid.x

        if not nearby_boids:
            return [500,500]

        x/=len(nearby_boids)
        y/=len(nearby_boids)
    
        return (x,y)



    def vector_towards_point(self,boid,point):
        vx=point[0]-boid.x
        vy=point[1]-boid.y
        vector=Vector2(vx,vy)
        if vector.length()<=0:
            return (boid.sx,boid.sy)
        vector.scale_to_length(5)
        return vector


    #Returns average direction of nearby boids
    def get_average_direction(self,nearby_boids):
        sy=1
        sx=1
        for boid in nearby_boids:
            sy+=boid.sy
            sx+=boid.sx
        
        if not nearby_boids:
            return (self.screen_x/2,self.screen_y/2)

        sx/=len(nearby_boids)
        sy/=len(nearby_boids)
        vector=Vector2(sx,sy)
        vector.scale_to_length(5)
        return vector
        
    def moveBoid(self,boid):
        self.keep_in_screen(boid)

    def moveHoik(self,boid):
        self.keep_in_screen(boid)


    # def keep_in_screen(self,moveObject):
    #     acceptable_distance=100

    #     if moveObject.x+moveObject.width>=self.screen_x-acceptable_distance:
    #         moveObject.sx,moveObject.sy=self.vector_towards_point(moveObject,(self.screen_x/2,self.screen_y/2))
        
    #     if moveObject.x<=acceptable_distance:
    #         moveObject.sx,moveObject.sy=self.vector_towards_point(moveObject,(self.screen_x/2,self.screen_y/2))

    #     if moveObject.y+moveObject.height>=self.screen_y-acceptable_distance:
    #         moveObject.sx,moveObject.sy=self.vector_towards_point(moveObject,(self.screen_x/2,self.screen_y/2))

    #     if moveObject.y<=acceptable_distance:
    #         moveObject.sx,moveObject.sy=self.vector_towards_point(moveObject,(self.screen_x/2,self.screen_y/2))


    def repell_from_obstacles(self,obstacles,boid):
        shortestDistance=9999
        nearestObstacle=0
        for obstacle in obstacles:
            sx=abs(boid.x-obstacle.x)
            sy=abs(boid.y-obstacle.y)
            if shortestDistance > sx+sy:
                shortestDistance=sx+sy
                nearestObstacle=obstacle            
        
        if shortestDistance<=100:
            vector = Vector2(self.vector_towards_point(boid,nearestObstacle.get_middle_point()))
            vector.scale_to_length(5)
            vector=vector*-1
            boid.sx,boid.sy=self.getAverageVector(vector,(boid.sx,boid.sy))


    def repell_from_nearest_moveobject(self,boid,boid_list):
        nearestBoid = boid
        shortestDistance=9999
        for b in boid_list:
            sx=abs(boid.x-b.x)
            sy=abs(boid.y-b.y)
            if shortestDistance > sx+sy:
                shortestDistance=sx+sy
                nearestBoid=b
        if shortestDistance<=75:
            vector=Vector2(self.vector_towards_point(nearestBoid,(boid.x,boid.y)))
            boid.sx,boid.sy=self.getAverageVector((boid.sx,boid.sy),(vector))
        #exit(3)
        #return nearestBoid


    def keep_in_screen(self,moveObject):
        if moveObject.x+moveObject.width>=self.screen_x:
            moveObject.x=self.screen_x-moveObject.width
            moveObject.sx*=-1

        if moveObject.x<=0:
            moveObject.x=0
            moveObject.sx*=-1

        if moveObject.y+moveObject.height>=self.screen_y:
            moveObject.y=self.screen_y-moveObject.height
            moveObject.sy*=-1

        if moveObject.y<=0:
            moveObject.y=0
            moveObject.sy*=-1

    def getAverageVector(self, vector1,vector2):
        avg=Vector2((vector1[0]+vector2[0])/2,(vector1[1]+vector2[1])/2)
        if avg.length()<=0:
            return vector1
        avg.scale_to_length(5)
        return avg

