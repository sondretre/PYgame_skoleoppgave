import os
import sys
import pygame
from pygame.locals import *
import settings
#import Test_Utility
# Importerer bare ed classene vi trenger fra sprites filen
from Test_Sprites import StaticElement, MovingElement, BouncingElement, PlayerElement

pygame.display.set_caption("The Ture Game")
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))