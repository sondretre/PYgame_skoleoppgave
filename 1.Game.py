import os
import sys
import pygame
from pygame.locals import *
#import 1.utility
#import sprites
from ASprites import Wall, Player, Room, Room1

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)


#//
SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 700

pygame.init()

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('DA game')

#background = pygame.Surface(screen.get_size())

#background.fill(black)

#player = Player(50, 50)
#movingsprite = pygame.sprite.Group()
#movingsprite.add(player)

rooms = []

room = Room1()
rooms.append(room)

current_room_no = 0
current_room = rooms[current_room_no]

player = Player(current_room)

player.rect.x = 340
player.rect.y = SCREEN_HEIGHT - player.rect.height
movingsprite = pygame.sprite.Group()
movingsprite.add(player)

clock = pygame.time.Clock()
score = 0

done = False

while not done:
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.go_left()
            if event.key == K_RIGHT:
                player.go_right()
            if event.key == K_UP:
                player.jump()

        if event.type == KEYUP:
            if event.key == K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == K_RIGHT and player.change_x > 0:
                player.stop()

        if event.type == KEYDOWN:
            if event.key == K_UP and player.change_y < 0:
                player.stop()



    movingsprite.update()
        
    if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 890
            elif current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 890
    
    if player.rect.x > 901:
            if current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 0:
                current_room_no = 0
                current_room = rooms[current_room_no]

    

    movingsprite.draw(screen)
    #movingsprite.update()
    current_room.wall_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                player.changespeed(-5,0)
#            elif event.key == pygame.K_RIGHT:
#                player.changespeed(5,0)
#            elif event.key == pygame.K_UP:
#                player.changespeed(0,-5)
#            elif event.key == pygame.K_DOWN:
#                player.changespeed(0,5)

        
#        elif event.type == pygame.KEYUP:
#            if event.key == pygame.K_LEFT:
#                player.changespeed(5,0)
#            elif event.key == pygame.K_RIGHT:
#                player.changespeed(-5,0)
##            elif event.key == pygame.K_UP:
#                player.changespeed(0,5)
#            elif event.key == pygame.K_DOWN:
#                player.changespeed(0,-5)
#        
#        player.update(current_room.wall_list)
