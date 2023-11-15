import pygame
from archconst import *
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #TODO flip the fish if going the other way
        super().__init__()
        self.forward_image=pygame.image.load("../assets/sprites/soldier_stand.png")
        self.reverse_image=pygame.transform.flip(self.forward_image,True,False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1*PLAYER_SPEED
    def move_down(self):
        self.y_speed=PLAYER_SPEED
    def move_left(self):
        self.x_speed=-1*PLAYER_SPEED
        self.image=self.reverse_image
    def move_right(self):
        self.x_speed=PLAYER_SPEED
        self.image=self.forward_image
    def stop(self):
        self.x_speed = 0
        self.y_speed = 0
        print(self.rect.x,self.rect.y)
        print(self.rect.center)
    def update(self):
        #TODO:Make sure orange fish stays on screen
        self.x+=self.x_speed
        self.y+=self.y_speed

        if self.x>SCREEN_WIDTH-TILE_SIZE:
            self.x=SCREEN_WIDTH-TILE_SIZE
        if self.x<0:
            self.x=0
        if self.y>SCREEN_HEIGHT-2*TILE_SIZE:
            self.y=SCREEN_HEIGHT-2*TILE_SIZE
        if self.y<0:
            self.y=0
        self.rect.x=self.x
        self.rect.y=self.y


    def draw(self,surf):
        surf.blit(self.image,self.rect)