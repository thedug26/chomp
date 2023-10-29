import pygame
import random
import sys
from background import draw_background
from game_parameters import *

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Collecting Pygame Events')
custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", 128)
running=True
background=screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print("you pressed the up key")
            if event.key==pygame.K_DOWN:
                print("you pressed the down key")
            if event.key==pygame.K_LEFT:
                print("you pressed the left key")
            if event.key==pygame.K_RIGHT:
                print("you pressed the right key")
            if event.key==pygame.K_p:
                print("you pressed the p key")


    screen.blit(background,(0,0))

    pygame.display.flip()


pygame.quit()
sys.exit()

