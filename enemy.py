import pygame
import random
import math
pygame.init()  
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

enemyImage,enemyX,enemyY,enemyX_change,enemyY_change = [],[],[],[],[]
num_of_enemies = 200
change=-100
def enemy1(position,change):
    for i in range(num_of_enemies):
        enemyImage.append(pygame.image.load("assets/baby-car (1).png"))
        #enemyX.append(random.randint(0, 736))
        #enemyY.append(random.randint(100, 00))
        enemyX.append(change)
        possiblepositons =[position]
        enemyY.append(possiblepositons[random.randrange(0,1)])
        enemyX_change.append(0.3)
        enemyY_change.append(0.3)
        change+=-200

def is_colission(enemyX,enemyY,playerX,playerY):
    distance = math.sqrt((math.pow(enemyX-playerX,2)) + (math.pow(enemyY-playerY,2)))
    if distance<30:
        return True
    else:
        return False    

def enemyy(playerX,playerY):
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        #if enemyX[i] <= 0:
            #enemyX_change[i] = 0.4
            #enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 800:
            enemyX_change[i] = 0.3
            enemyX[i]=-1
            enemyY[i] += enemyY_change[i]
        colision = is_colission(enemyX[i],enemyY[i],playerX,playerY)
        if colision:
            stop = True
        enemy(enemyX[i],enemyY[i],i) 

def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y)) 
