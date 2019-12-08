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


#//
score = 0

pygame.init()

screen = pygame.display.set_mode([800, 600])

pygame.display.set_caption('test')

background = pygame.Surface(screen.get_size())

background.fill(black)

player = Player(50, 50)
all_sprite_list = pygame.sprite.Group()
all_sprite_list.add(player)

wall_list = pygame.sprite.Group()

wall = Wall(0,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10,0,790,10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10,200,100,10)
wall_list.add(wall)
all_sprite_list.add(wall)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3.0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3.0)
            elif event.key == pygame.K_UP:
                player.changespeed(0.-3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0.3)

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3.0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3.0)
            elif event.key == pygame.K_UP:
                player.changespeed(0.3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0.-3)
    player.update(wall_list)

    screen.fill(black)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(40)

pygame.quit()


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
    