import pygame
import sys
import math
from backarcher import *
from archconst import *

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ballistic Projectiles with Angles and Gravity in Pygame")

# Colors
#white = (255, 255, 255)
black = (0, 0, 0)
#red = (255, 0, 0)

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.image.load("../Archer_Game/assets/Archer_Sprites/arrow.png")
        #self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = math.radians(angle)
        self.speed = 10

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)
        self.speed += gravity

        # Check if the projectile is out of the screen
        if self.rect.y > SCREEN_HEIGHT or self.rect.x < 0 or self.rect.x > SCREEN_WIDTH:
            self.kill()


# Cannon class
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../Archer_Game/assets/Archer_Sprites/adventurer_hold1.png")
        #self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (player1x, SCREEN_HEIGHT - 2*TILE_SIZE)

# Gravity
gravity = 0.1

# Sprite groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Create cannon
cannon = Cannon()
all_sprites.add(cannon)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot a projectile when the spacebar is pressed
                angle = 45  # Initial launch angle
                projectile = Projectile(cannon.rect.centerx, cannon.rect.centery, angle)
                all_sprites.add(projectile)
                projectiles.add(projectile)

    all_sprites.update()

    # Draw everything
    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)


