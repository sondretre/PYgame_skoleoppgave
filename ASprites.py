#endre til class fill

import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,150,0)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(blue)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        
        width = 40
        height = 60
        self.image = pygame.Surface([15, 15])
        self.image.fill(white)

        self.rect = self.image.get_rect()
        
    def update(self):

        self.calc_grav()

        self.rect.x +=self.change_x
        pos = self.rect.x

        block_hit_list = pygame.sprite.spritecollide(self, wall, False)
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

            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and seld.change_y >= 0:
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):

        self.rect.y += 2
        wall_hit_list = pygame.sprite.spritecollide(self, walls, False)
        self.rect.y -= 2

        if len(wall_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):

        self.change_x = -6

    def go_right(self):
        
        self.change_x = 6

    def stop(self):
        self.change_x = 0

#        self.rect.y = y
#        self.rect.x = x

#    def changespeed(self, x, y):
#        self.change_x += x
#        self.change_y += y
    
#    def move(self, walls):

#        self.rect.x += self.change_x

#        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
#        for block in block_hit_list:

#            if self.change_x > 0:
#                self.rect.right = block.rect.left
#            else:
#                self.rect.left = block.rect.right
            
#        self.rect.y += self.change_y

#        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
#        for block in block_hit_list:
#
#            if self.change_y > 0:
#                self.rect.bottom = block.rect.top
#            else:
#                self.rect.top = block.rect.bottom

class Room():

    wall_list = None
    coin_sprites = None

    def __init__(self):
        #lager lister
        self.wall_list = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()

class Room1(Room):
    
    def __init__(self):
        Room.__init__(self)
        # Liste over vegger: x,y,lengde, høgde, farge
        walls = [ [0,690,1000,10,blue],
                  [50,0,0,0,blue],
                  [0,0,0,0,blue],
                  [0,0,0,0,blue],
                  [0,0,0,10,blue],
                  [0,0,0,0,blue],
                  [0,0,0,0,blue],
                  [0,0,0,0,blue],
                  [0,0,0,0,blue]
                ]
        
        for item in walls:
            wall=Wall(item[0],item[1],item[2],item[3],item[4])
            self.wall_list.add(wall)





