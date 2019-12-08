import os
import sys
import random
import pygame
import math
from pygame.locals import *
#import 1.Settings
#import 1.utility

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([15, 15])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    def update(self, walls):

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom




#class Element(pygame.sprite.Sprite):
#    def __init__(self, graphic):
#        pygame.sprite.Sprite.__init__(self)
#        filename = os.path.join(settings.ASSETS_DIR, graphic['filename'])
#        self.image = Utility.load_image(filename, graphic['size'])
#        self.rect = self.image.get_rect()
#
#    def update(self):
#        if settings.DEBUG:
#            draw_rect = self.rect
#            draw_rect = pygame.rect.Rect(0,0, self.rect.width-1, self.rect.height -1)
#            pygame.draw.rect(self.image, (0, 0, 0), draw_rect, 1)
#
#class StaticElement(Element):
#    def __init__(self, graphic, position):
#        Element.__init__(self, graphic)
#        self.rect.left = position[0]
#        self.rect.top = position[1]
#    
#class MovingElement(StaticElement):
#    def __init__(self, graphic, position, speed):
#        StaticElement.__init__(self, graphic, position)
#        self.dx = speed[0]
#        self.dy = speed[1]
#
#    def update(self):
#        StaticElement.update(self)
#        self.rect.left += self.dx
#        self.rect.top += self.dy
#
#class BouncingElement(MovingElement):
#    def update(self):
#        MovingElement.update(self)
#        if (self.rect.left <= 0) or (self.rect.right > settings.SCREEN_WIDTH):
#            self.dx *= -1
#        
#        if (self.rect.top <= 0) or (self.rect.bottom >= settings.SCREEN_HEIGHT):
#            self.dy *= -1

#class PlayerElement(MovingElement):
#    def __init__(self, graphic, position, speed):
#        MovingElement.__init__(self, graphic, position, speed)
#        self.dx = speed[1]
#        self.dy = speed[1]
#    def update(self):
#        MovingElement.update(self)
#
#    def move_left(pixler):
#        self.rect.left -= pixler
#
#    def move_right(pixler):
#        self.rect.right -= pixler
    