import pygame
import os
import sys
from pygame.locals import *

#her importerer jeg key bindings

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        50 -= 5

    if keys[pygame.K_RIGHT]:
        50 += 5

    if keys[pygame.K_UP]:
        50 -= 5

    if keys[pygame.K_DOWN]:
        50 += 5