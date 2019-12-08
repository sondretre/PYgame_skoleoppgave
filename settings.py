import pygame


DEBUG = True

FPS = 60

#Lager nav til filen
pygame.display.set_caption("The Ture Game")

#definerer swindustørelsen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

Gravity = 1


ASSETS_DIR = 'Game_Art'
#Art-assets
#her henter jeg art assets

Platform        = {'filename' : 'Platform.png', 'size' : (237,36)}
Player_carakter = {'filename' : 'playyer.png' , 'size' : (63,150)}
Enemy_1         = {'filename' : 'oofton.png'  , 'size' : (92,140)}
Enemy_2         = {'filename' : 'Slime.png'   , 'size' : (78,42)}
Ground          = {'filename' : 'Test_ground' , 'size' : (569,55)}
Backround       = {'filename' : 'Landskap.png', 'size' : (580,326)}
coin            = {'filename' : 'Coin.png'    , 'size' : (30,30)}