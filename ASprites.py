#endre til class fill

import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

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
    
    def move(self, walls):

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
        # Liste over vegger: x,y,lengde og høgde
        walls = [ [1,590,1000,10,blue],
                  [50,400,200,10,blue],
                  [600,400,200,10,blue]
                ]
        
        for item in walls:
            wall=Wall(item[0],item[1],item[2],item[3],item[4])
            self.wall_list.add(wall)

class Room2(Room):
    def __init__(self):
        Room.__init__(self)

        walls = [ [590,700,1,10,blue],
                  [50,600,200,100,blue],
                  [600,750,100,100,blue],
                  #[x,x,x,x,color],
                  #[x,x,x,x,color]
                ]
        
        for item in walls:
            wall=Wall(item[0],item[1],item[2],item[3],item[4])
            self.wall_list.add(wall)




