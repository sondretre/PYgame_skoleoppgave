import os
import sys
import pygame
from pygame.locals import *
import settings
import Utility
# Med import henter jeg filer og med from henter jeg spesefike ting
from Sprites import StaticElement, MovingElement, BouncingElement, PlayerElement

# Sentrerer pygame vindu
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initaliserer pygame mondulen
pygame.init()
clock = pygame.time.Clock()
pygame.font.init() # Initaliserer fonter

pygame.key.set_repeat(10, 10)

#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.DOUBLEBUF) 
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)) 
surface = pygame.Surface(screen.get_size())
surface.convert()

elements = pygame.sprite.Group()

elements.add(StaticElement(settings.Platform, (100, 100)))
elements.add(StaticElement(settings.Platform, (200, 200)))

elements.add(MovingElement(settings.Enemy_1, (0, 0), (2,2)))
elements.add(MovingElement(settings.Enemy_2, (0, 0), (2,1)))

#elements.add(MovingElement(settings.ITEM_ENEMY_BLOCK_RED, (0, 0), (2,2)))

elements.add(PlayerElement(settings.Player_carakter, (0, 300), (2,0)))

elements.add(BouncingElement(settings.Enemy_2, (500, 0), (0,2)))

#elements.add(BouncingElement(settings.Cha, (0, 0), (2,2)))


while True:
    pygame.event.pump()
    for event in pygame.event.get():
        # Avslutter ved Window X eller Q tast
        if (event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or ((event.type == KEYDOWN) and (event.key == K_q)):
            pygame.quit()   
            sys.exit()

        #Når pil venstre trykkes
        #element_good.sprite.move_left()

    surface.fill((255, 255, 255))
    
    elements.update()
    elements.draw(surface)

    screen.blit(surface, (0,0))
 
    pygame.display.flip()
    pygame.display.update()
    clock.tick(settings.FPS)
    # Sjekker om vi traff topp eller bunn av skjermen