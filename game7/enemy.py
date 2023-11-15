import pygame
import random
from game_parameters import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load("../assets/sprites/puffer_fish.png").convert()

        self.image.set_colorkey((0,0,0))

        self.image=pygame.transform.flip(self.image,True,False)

        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.speed=random.uniform(MAX_SPEED-1,MAX_SPEED)
        self.rect.center=(x,y)

    def update(self):
        self.x-=self.speed
        self.rect.x=self.x

    def draw(self,surf):
        surf.blit(self.image, self.rect)

enemies=pygame.sprite.Group()