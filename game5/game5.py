import pygame
import random
import sys

from game_parameters import *
from fish import Fish, fishes
from background import draw_background
from player import Player


#initialize pygame
pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adding a player fish on the screen')
clock=pygame.time.Clock()

running=True
background=screen.copy()
draw_background(background)

for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH,SCREEN_WIDTH*1.5),random.randint(TILE_SIZE,SCREEN_HEIGHT-2*TILE_SIZE)))

player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        player.stop()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                print("you pressed the up key")
                player.move_up()
            if event.key==pygame.K_DOWN:
                print("you pressed the down key")
                player.move_down()
            if event.key==pygame.K_LEFT:
                print("you pressed the left key")
                player.move_left()
            if event.key==pygame.K_RIGHT:
                print("you pressed the right key")
                player.move_right()
            if event.key==pygame.K_p:
                print("you pressed the p key")

    screen.blit(background, (0, 0))
    fishes.update()

    player.update()
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))
    fishes.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

    fishes.update()

pygame.quit()
sys.exit()