import pygame
import math
import random
#iniciating code
pygame.init()  
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("assets/Frogger")
icon = pygame.image.load("assets/frog (1).png")
pygame.display.set_icon(icon)

#background
background= pygame.image.load("assets/froggerbg.png")

    
#player
playerImage = pygame.image.load("assets/frog.png")
playerX= 370
playerY =560
playerX_change = 0
playerY_change = 0

#enemy
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =[]
num_of_enemies = 3
change=-10
for i in range(num_of_enemies):
    enemyImage.append(pygame.image.load("assets/baby-car (1).png"))
    #enemyX.append(random.randint(0, 736))
    #enemyY.append(random.randint(100, 00))
    enemyX.append(change)
    possiblepositons =[300]
    enemyY.append(possiblepositons[random.randrange(0,1)])
    enemyX_change.append(0.3)
    enemyY_change.append(0.3)
    change-=20
enemy1Image = []
enemy1X = []
enemy1Y = []
enemy1X_change = []
enemy1Y_change =[]
num_of_enemies = 3
change=0.3
for i in range(num_of_enemies):
    enemy1Image.append(pygame.image.load("assets/baby-car (1).png"))
    #enemyX.append(random.randint(0, 736))
    #enemyY.append(random.randint(100, 00))
    enemy1X.append(0)
    possiblepositons =[400]
    enemy1Y.append(possiblepositons[random.randrange(0,1)])
    enemy1X_change.append(change)
    enemy1Y_change.append(change)
    change+=0.3
def player(x,y):
    screen.blit(playerImage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y)) 
def enemy1(x,y,i):
    screen.blit(enemy1Image[i],(x,y))     
def is_colission(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2)))
    if distance<30:
        return True
    else:
        return False
def is_colission(enemy1X,enemy1Y,playerX,playerY):
    distance = math.sqrt((math.pow(enemy1X-playerX,2)) + (math.pow(enemy1Y-playerY,2)))
    if distance<30:
        return True
    else:
        return False
running = True
stop = False
#loop main code
while running:
    screen.fill((0,0,200)) 
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change =- 0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        if stop:
            playerX=370
            playerY = 570
        stop=False
    #changing according pressed keys
    
    playerX += playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=768:
        playerX=768
    playerY +=playerY_change
    if playerY<=0:
        playerY=0
    elif playerY>=568:
        playerY = 568
    #Enemy Mov
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]          
        if enemyX[i] <= -1.5:
            enemyX_change[i] = 0.0
          
        elif enemyX[i] >= 800:
            enemyX_change[i] = 0.0
    for i in range(num_of_enemies):
        enemy1X[i] += enemy1X_change[i]          
        if enemy1X[i] <= -1.5:
            enemy1X_change[i] = 0.0
          
        elif enemy1X[i] >= 800:
            enemy1X_change[i] = 0.0
                    


        colision = is_colission(enemyX[i],enemyY[i],playerX,playerY)
        colision = is_colission(enemy1X[i],enemy1Y[i],playerX,playerY)
        if colision:
          
            stop = True
        enemy(enemyX[i],enemyY[i],i)   
        enemy1(enemy1X[i],enemy1Y[i],i)   
    
    #inicializating functions
    player(playerX,playerY) 
    pygame.display.update()