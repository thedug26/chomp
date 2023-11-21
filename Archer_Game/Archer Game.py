import sys
from backarcher import *
from archer_player import *

#from position import Position

#initialize game
pygame.init()

#background
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Archer Game Beta')
clock=pygame.time.Clock()

#player=Players()
#player_group=pygame.sprite.Group()
#player_group.add(player)

#bullet_group=pygame.sprite.Group()

current_time=0
button_press_time=0


running=True
background=screen.copy()
draw_background(background)

soldier = Player(player1x, SCREEN_HEIGHT - TILE_SIZE * 5 -5)
#print(soldier.rect.width, soldier.rect.height)
adventurer = Player(player2x, SCREEN_HEIGHT - TILE_SIZE * 5 -5)

#soldier_shoot=Bullet(soldier.self.x,soldier.self.y)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONUP:
            button_press_time = pygame.time.get_ticks()
            soldier.pos_update(current_time)
            adventurer.pos_update1(current_time)
            #soldier.draw(screen)
            print("click")

        current_time = pygame.time.get_ticks()


    screen.blit(background, (0, 0))


    soldier.draw(screen)
    adventurer.draw2(screen)
    soldier.update()
    adventurer.update()



    #text = score_font.render(f'{score}', True, (255, 0, 0))

    #screen.blit(text,(SCREEN_WIDTH-TILE_SIZE,0))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()



#timing info

