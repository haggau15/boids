from pygame import Vector2
import pygame

from block import block
#All the blocks are made and put into a list here
class setupblocks():
    def setup():
        height = 240
        width = 60
        spacing_x=256
        spacing_y=64
        red=(255,0,0)
        blue=(0,0,255)
        green=(0,255,0)
        blocks=[]
        
        blocks.append(block(blue,0,0,          height,width,1))
        blocks.append(block(blue,spacing_x,  0,height,width,1))
        blocks.append(block(blue,spacing_x*2,0,height,width,1))
        blocks.append(block(blue,spacing_x*3,0,height,width,1))
        blocks.append(block(blue,spacing_x*4,0,height,width,1))
        
        blocks.append(block(red,0,          spacing_y,height,width,0))
        blocks.append(block(red,spacing_x,  spacing_y,height,width,0))
        blocks.append(block(red,spacing_x*2,spacing_y,height,width,0))
        blocks.append(block(red,spacing_x*3,spacing_y,height,width,0))
        blocks.append(block(red,spacing_x*4,spacing_y,height,width,0))
        
        blocks.append(block(green,0,          spacing_y*2,height,width,0))
        blocks.append(block(green,spacing_x,  spacing_y*2,height,width,0))
        blocks.append(block(green,spacing_x*2,spacing_y*2,height,width,0))
        blocks.append(block(green,spacing_x*3,spacing_y*2,height,width,0))
        blocks.append(block(green,spacing_x*4,spacing_y*2,height,width,0))

        return blocks
