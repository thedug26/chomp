import pygame
import sys
import random
pygame.init()

screen_width=800
screen_height=600
tile_size=64

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Beach')

custom_font= pygame.font.Font("assets/fonts/Brainfish_Rush.ttf",128)
def draw_background(surf):
    water=pygame.image.load("assets/sprites/water.png").convert()
    sand=pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass=pygame.image.load("assets/sprites/seagrass.png").convert()

    sand.set_colorkey((0,0,0))
    seagrass.set_colorkey((0,0,0))

    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_height,tile_size):
            surf.blit(water,(x,y))

    for x in range(0,screen_width,tile_size):
        surf.blit(sand,(x,screen_height-tile_size))

    for _ in range(5):
        x=random.randint(0,screen_width)
        surf.blit(seagrass,(x,screen_height-tile_size*2))

        text=custom_font.render("Chomp",True,(255,0,0))
        surf.blit(text, (screen_width/2-text.get_width()/2, text.get_height()/100))

def draw_fishes(surf):

    green_fish=pygame.image.load("assets/sprites/green_fish.png").convert()
    green_fish.set_colorkey((0,0,0))
    green_fish=pygame.transform.flip(green_fish,True,False)
    orange_fish=pygame.image.load("assets/sprites/orange_fish.png").convert()
    orange_fish.set_colorkey((0,0,0))
    for _ in range(5):
        x= random.randint(0,screen_width-tile_size)
        y=random.randint(tile_size*1.5,screen_height-2*tile_size)
        x1 = random.randint(0, screen_width - tile_size)
        y1 = random.randint(tile_size, screen_height - 2*tile_size)
        surf.blit(green_fish,(x,y))
        surf.blit(orange_fish,(x1,y1))
running=True
background=screen.copy()
draw_background(background)
draw_fishes(background)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background,(0,0))
    pygame.display.flip()
pygame.quit()