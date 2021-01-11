import pygame
import random
import os
import math

base_path = os.path.dirname(__file__)

# Initialize pygame
pygame.init()

# Create the game screen
screen = pygame.display.set_mode((800,600))

# Background
bg = pygame.image.load("space-bg.gif")

# Title and Icon
pygame.display.set_caption("Space Invaders")
#icon_path = os.path.join(base_path, "assets/ufo.png")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Spaceship
#ss_path = os.path.join(base_path, "assets/spaceship.png")
ssImg = pygame.image.load("spaceship.png")
ssX = 370
ssY = 480
ssX_change = 0
ssY_change = 0

# Enemy
#enemy_path = os.path.join(base_path, "assets/enemy.png")
enemyImg = pygame.image.load("enemy.png")
eX = random.randint(0,800)
eY = random.randint(50,150)
eX_change = 0.2
eY_change = 40

# Bullet
#enemy_path = os.path.join(base_path, "assets/enemy.png")
bulletImg = pygame.image.load("bullet.png")
bX = 0
bY = 0
bX_change = 0
bY_change = 1
b_state = "ready"

score = 0

# Player method
def player(x,y):
    # Draws an image of the player
    screen.blit(ssImg, (x, y))

# Player method
def enemy(x,y):
    # Draws an image of the player
    screen.blit(enemyImg, (x, y))

def bullet_fire(x,y):
    global b_state
    b_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Collision checker
def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX-bX, 2)) + (math.pow(eY-bY,2)))
    if distance < 27:
        return True
    else:
        return False

# Condition for the game to keep running
run_game = True

while run_game:
    
    screen.fill((0,0,0))

    screen.blit(bg,(0,0))

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
            if event.key == pygame.K_SPACE:
                if b_state == "ready":
                    bX = ssX
                    bY = ssY
                    bullet_fire(bX,bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ssX_change = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ssY_change = 0

    # Changing the position of the spaceship
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

    # Changing the position of the enemy
    eX += eX_change

    if eX <=0:
        eX_change = 0.2
        eY += eY_change
    elif eX >= 736:
        eX_change = -0.2
        eY += eY_change


    if bY <=0:
        bY = 480
        b_state = "ready"

    if b_state == "fire":
        bullet_fire(bX,bY)
        bY -= bY_change


    collision = isCollision(eX,eY,bX,bY)
    if collision:
        bY = 480
        b_state = "ready"
        score += 1
        print(score)
        eX = random.randint(0,735)
        eY = random.randint(50,150)


    player(ssX,ssY)
    enemy(eX,eY)
    pygame.display.update()