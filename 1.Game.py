import os
import sys
import pygame
from pygame.locals import *
#import 1.utility
#import sprites
from ASprites import Wall, Player

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

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
                player.changespeed(-3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,-3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,3)

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,-3)
    player.update(wall_list)

    screen.fill(black)

    all_sprite_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
