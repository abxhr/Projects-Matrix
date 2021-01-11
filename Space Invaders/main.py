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
enemyImg = []
eX = []
eY = []
eX_change = []
eY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    eX.append(random.randint(0,800))
    eY.append(random.randint(50,150))
    eX_change.append(0.2)
    eY_change.append(40)

# Bullet
#enemy_path = os.path.join(base_path, "assets/enemy.png")
bulletImg = pygame.image.load("bullet.png")
bX = 0
bY = 0
bX_change = 0
bY_change = 1
b_state = "ready"

# Score
score_val = 0
font = pygame.font.Font('ARCADECLASSIC.ttf',32)
textX = 10
textY = 10

def getScore(x,y):
    score = font.render("Score =  "+ str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))

# Player method
def player(x,y):
    # Draws an image of the player
    screen.blit(ssImg, (x, y))

# Player method
def enemy(x,y,i):
    # Draws an image of the player
    screen.blit(enemyImg[i], (x, y))

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
    
    for i in range(no_of_enemies): 
        eX[i] += eX_change[i]
        if eX[i] <=0:
            eX_change[i] = 0.2
            eY[i] += eY_change[i]
        elif eX[i] >= 736:
            eX_change[i] = -0.2
            eY[i] += eY_change[i]

        collision = isCollision(eX[i],eY[i],bX,bY)
        if collision:
            bY = ssY
            b_state = "ready"
            score_val += 1
            eX[i] = random.randint(0,735)
            eY[i] = random.randint(50,150)

        enemy(eX[i],eY[i],i)

    if bY <=0:
        bY = 480
        b_state = "ready"

    if b_state == "fire":
        bullet_fire(bX,bY)
        bY -= bY_change

    player(ssX,ssY)
    getScore(textX,textY)
    pygame.display.update()