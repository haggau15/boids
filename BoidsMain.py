from pygame import Vector2
import pygame
from InitObjects import InitObjects
from Move import Move
import random
screen_x=1000
screen_y=1000

move=Move(screen_x,screen_y)
initobjects=InitObjects(screen_x,screen_y)
pygame.init()
screen_res = (screen_x,screen_y)
screen = pygame.display.set_mode(screen_res)
clock = pygame.time.Clock()
boidlist=initobjects.GetBoids()
hoiklist=initobjects.GetHoiks()
obstaclelist=initobjects.GetObstacles()
nearbyboids=[]

while True:
    pygame.display.update()
    screen.fill((12,12,48))

    for hoik in hoiklist:
        #move.repell_from_obstacles(obstaclelist,hoik)
        move.moveHoik(hoik)
        hoik.draw(screen)

    for obstacle in obstaclelist:
        obstacle.draw(screen)
   

    for boid in boidlist:
        nearbyboids.clear()
        for b in boidlist:
            if abs(boid.x-b.x)<100 and abs(boid.y-b.y)<100 and b!=boid:
                nearbyboids.append(b)          

        move.get_average_pos(nearbyboids)
        boid.sx, boid.sy = move.get_average_direction(nearbyboids)
        move.repell_from_nearest_moveobject(boid,nearbyboids)
        move.repell_from_nearest_moveobject(boid,hoiklist)
        move.repell_from_obstacles(obstaclelist,boid)
        move.moveBoid(boid)
        boid.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()
    clock.tick(30)



    