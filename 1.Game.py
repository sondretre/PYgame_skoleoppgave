import os
import sys
import pygame
from pygame.locals import *
#import 1.utility
#import sprites
from ASprites import Wall, Player, Room, Room1, Room2

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

#//

pygame.init()

screen = pygame.display.set_mode([900, 700])

pygame.display.set_caption('test')

#background = pygame.Surface(screen.get_size())

#background.fill(black)

player = Player(50, 50)
movingsprite = pygame.sprite.Group()
movingsprite.add(player)

rooms = []

room = Room1()
rooms.append(room)

room = Room2()
rooms.append(room)

current_room_no = 0
current_room = rooms[current_room_no]

clock = pygame.time.Clock()
score = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,-5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,5)

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5,0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-5,0)
            elif event.key == pygame.K_UP:
                player.changespeed(0,5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0,-5)
        
        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 1:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
    
        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no == 1
                current_room_no = 0
                current_room = rooms[current_room_no]

    screen.fill(black)

    movingsprite.draw(screen)
    current_room.wall_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
