import pygame
import random

# Initialize pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Spaceship
ssImg = pygame.image.load("spaceship.png")
ssX = 370
ssY = 480
ssX_change = 0
ssY_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
eX = random.randint(0,800)
eY = random.randint(50,150)
eX_change = 0
eY_change = 0

# Player method
def player(x,y):
    # Draws an image of the player
    screen.blit(ssImg, (x, y))

# Player method
def enemy(x,y):
    # Draws an image of the player
    screen.blit(enemyImg, (x, y))

# Condition for the game to keep running
run_game = True

while run_game:
    
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ssX_change = -0.2
            if event.key == pygame.K_RIGHT:
                ssX_change = 0.2
            if event.key == pygame.K_UP:
                ssY_change = -0.2
            if event.key == pygame.K_DOWN:
                ssY_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ssX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ssY_change = 0

    ssX += ssX_change
    ssY += ssY_change

    if ssX <= 0:
        ssX = 0
    elif ssX >= 736:
        ssX = 736

    if ssY >= 536: 
        ssY = 536
    elif ssY <= 0:
        ssY = 0

    player(ssX,ssY)
    enemy(eX,eY)
    pygame.display.update()