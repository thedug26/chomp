import pygame
import sys
pygame.init()

screen_width=800
screen_height=600

BLUE=(0,0,255)
BROWN=(224,161,52)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Blue Backround with Brown Rectangle')

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill(BLUE)

    rectangle_height=200
    pygame.draw.rect(screen,BROWN,(0,screen_height-rectangle_height,screen_width,rectangle_height))


    pygame.display.flip()

pygame.quit()
