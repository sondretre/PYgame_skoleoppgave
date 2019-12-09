#endre til class fill

import pygame

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
                self.rect.left = block.rect.right
                #self.rect.right = block.rect.left
            else:
                #self.rect.left = block.rect.right
                self.rect.right = block.rect.left
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom




