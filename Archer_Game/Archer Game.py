import pygame
from archconst import *
import sys
from backarcher import *
from archer_player import *

#initialize game
pygame.init()

#background
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Adding a player fish on the screen')
clock=pygame.time.Clock()

running=True
background=screen.copy()
draw_background(background)


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background, (0, 0))

    Player.draw(screen)
    #text = score_font.render(f'{score}', True, (255, 0, 0))

    #screen.blit(text,(SCREEN_WIDTH-TILE_SIZE,0))
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()




