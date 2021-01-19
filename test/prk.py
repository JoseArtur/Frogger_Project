import pygame
import math
import random
from sys import exit
from pygame.locals import *
#iniciating code
pygame.init()  
pygame.font.init()
#Fonts
font_name = pygame.font.get_default_font()
#####
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
#IMAGES
background_image="assets/froggerbg.png"
frog_image = "assets/frog.png"
car1_image = "assets/baby-car (1).png"
car2_image =  "assets/baby-car (1).png"
#more cars images
#wood image
pygame.display.set_caption("assets/Frogger")

# ICON
icon = pygame.image.load("assets/frog (1).png")
pygame.display.set_icon(icon)

#background and Sprites
background= pygame.image.load(background_image)
frog_sprite = pygame.image.load(frog_image)
car1_sprite = pygame.image.load(car1_image)
car2_sprite = pygame.image.load(car2_image)
class Sprite():
    def __init__(self,position,sprite):
        self.sprite = sprite
        self.position = position
    
    def draw(self):
        screen.blit(self.sprite,(self.position))
    def rect(self):
        return Rect(self.position[0],self.position[1],self.sprite.get_width(),self.sprite.get_heoght())
class Frogger(Sprite):
    def __init__(self,position,frog_sprite):
        self.sprite = frog_sprite
        self.position = position
        self.lives = 3
        self.way = "UP"
        self.can_move = 1
    def updateSprite(self,key_pressed):
        if self.direct != key_pressed:
            self.direct = key_pressed
            if self.direct == "up":
                frog_filename = ''
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.direct == "down":
                frog_filename = './images/sprite_sheets_down.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.direct == "left":
                frog_filename = './images/sprite_sheets_left.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()
            elif self.direct == "right":
                frog_filename = './images/sprite_sheets_right.png'
                self.sprite = pygame.image.load(frog_filename).convert_alpha()


    def moveFrog(self,key_pressed, key_up):
        #Tem que fazer o if das bordas da tela ainda
        #O movimento na horizontal ainda não ta certin
        if self.animation_counter == 0 :
            self.updateSprite(key_pressed)
        self.incAnimationCounter()
        if key_up == 1:
            if key_pressed == "up":
                if self.position[1] > 39:
                    self.position[1] = self.position[1]-13
            elif key_pressed == "down":
                if self.position[1] < 473:
                    self.position[1] = self.position[1]+13
            if key_pressed == "left":
                if self.position[0] > 2:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]-13
                    else:
                        self.position[0] = self.position[0]-14
            elif key_pressed == "right":
                if self.position[0] < 401:
                    if self.animation_counter == 2 :
                        self.position[0] = self.position[0]+13
                    else:
                        self.position[0] = self.position[0]+14

    def animateFrog(self,key_pressed,key_up):
        if self.animation_counter != 0 :
            if self.animation_tick <= 0 :
                self.moveFrog(key_pressed,key_up)
                self.animation_tick = 1
            else :
                self.animation_tick = self.animation_tick - 1

    def setPos(self,position):
        self.position = position

    def decLives(self):
        self.lives = self.lives - 1

    def cannotMove(self):
        self.can_move = 0

    def incAnimationCounter(self):
        self.animation_counter = self.animation_counter + 1
        if self.animation_counter == 3 :
            self.animation_counter = 0
            self.can_move = 1

    def frogDead(self,game):
        self.setPositionToInitialPosition()
        self.decLives()
        game.resetTime()
        self.animation_counter = 0
        self.animation_tick = 1
        self.way = "UP"
        self.can_move = 1

    def setPositionToInitialPosition(self):
        self.position = [207, 475]

    def draw(self):
        current_sprite = self.animation_counter * 30
        screen.blit(self.sprite,(self.position),(0 + current_sprite, 0, 30, 30 + current_sprite))

    def rect(self):
        return Rect(self.position[0],self.position[1],30,30)

class Enemy(Sprite):
    def __init__(self,position,enemy_sprite,direc,factor):
        self.sprite = enemy_sprite
        self.position = position
        self.direc = direc
        self.factor = factor
    def move(self,veloc):
        if self.direc =="R":
            self.position[0] = self.position[0]+ veloc*self.factor
        elif self.direc =="L":
            self.position[0] = self.position[0] -veloc*self.factor
class Game():
    def __init__(self,veloc,level):
        self.speed = speed
        self.veloc = veloc
        self.level = level
        self.init = 0
    def morespeed(self):
        self.speed = self.speed +1
    
def drawL(list):
    for i in list:
        i.draw()
def moveL(list,veloc):
    for i in list:
        i.move(veloc)
        
def newEnemys(list,enemys,game):
    for i,j in enumerate(list):
        list[i] = list[i]-1
        if j<= 0:
            if i ==0:
                list[0] = (10*game.veloc)/ game.level
                position_start = [-20,800]
                enemy = Enemy(position_start,car1_image,"R",1)
                enemys.append(enemy) 
def Change(enemys):
    enemy = random.choice(enemys)
    initialPosition = enemy.position[1]
    
    choice = random.randint(1,2)   
    if (choice %2 == 0) :
        enemy.position[1] = enemy.position[1] +40
    else:
        enemy.position[1]  = enemy.position -39           
    if enemy.position[1] >  436:
        enemy.position[1] =initialPosition
    elif enemy.position[1 ] < 280:
        enemy.position[1] = initialPosition
running = 0
while running == 0:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            running =1
    screen.blit(background, (0, 0))
    pygame.display.update()
while True:
    running = 1 
    game = Game(3,1)
    key_up = 1
    frog_iniposition = [207,460]
    frog = Frogger(frog_iniposition,frog_sprite)
    
    enemys =[]
    j_enemys = [30,0,30,0,60]
    j_time = 30
    pressed_keys = 0
    key_pressed = 0
    while frog.lives >0:
        if event.type == QUIT :
            exit()
        if event.type == KEYUP:
            key_up = 1
        if event.type == KEYDOWN:
            if key_up == 1 and frog.can_move ==1:
                key_pressed = pygame.key.name(event.key)
                Froggger.moveFrog(key_pressed,key_up)
                Frogger.cannotMove()
        newEnemys(j_enemys,enemys,game)
        moveL(enemys,game.veloc)
        screen.blit(background, (0, 0))
       # screen.blit(text_info1,(10,520))
        #screen.blit(text_info2,(250,520)) 
        random =random.randint(0,100)
        if(random % 100 == 0):
            Change(enemys)

        drawL(enemys)
        Frogger.animateFrog(key_pressed,key_up)
        Frogger.draw()
        pygame.display.update()
        
"""
while gameInit:
    for event in pygame.event.get():
        if event.type == QUIT :
            gameInit
                
#playe

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
num_of_enemies = 200
change=-100
def enemyy(position,change):
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
enemyy(300,-100)
enemyy(400,-100)


def player(x,y):
    screen.blit(playerImage,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y)) 
#def enemy1(x,y,i):
   # screen.blit(enemy1Image[i],(x,y))     
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
        return False"""
running = True
stop = False
#loop main code
while running:
    game = Game(3,1)
    key_up = 1
    frog_iniposition = [207,460]
    frog = Frogger(frog_iniposition,frog_sprite)
    
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
            enemyX_change[i] = 0.3
          
        elif enemyX[i] >= 800:
            enemyX_change[i] = 0.0
   


        colision = is_colission(enemyX[i],enemyY[i],playerX,playerY)
        #colision = is_colission(enemy1X[i],enemy1Y[i],playerX,playerY)
        if colision:
          
            stop = True
        enemy(enemyX[i],enemyY[i],i)   
        #enemy1(enemy1X[i],enemy1Y[i],i)   
    
    #inicializating functions
    player(playerX,playerY) 
    pygame.display.update()