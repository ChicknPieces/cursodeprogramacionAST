




#sudo dpkg - configure -a
#sudo apt-get install python3 pygame

import math 
import random
import pygame
from pygame import mixer


#incio 
pygame.int()


#fondo
screen = pygame.display.set_mode((1000,800))

background= pygame.image.load('/home/pc18/Documentos/Trabajiño AST/Fondote.webp')

#sonido
# / mixer.music.load('')
# / mixer.music.play

# titulo e icono
pygame.display.set_caption("zapateros del campito contrap putos clavos en medio del pasto")
icon = pygame.image.load("/home/pc18/Documentos/Trabajiño AST/Pelsonaje-removebg-preview.png")
pygame.display.set_icon(icon)

# jugadores
playerImg=pygame.image.load("/home/pc18/Documentos/Trabajiño AST/zapatero-removebg-preview(1).png")
playerx = 370
playery = 480
playerx_change=0

#enemigo

enemyImg=[]
enemyX =[]
enemyY =[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies= 15

for I in range (num_of_enemies):
    enemyImg.append(pygame.image.load('/home/pc18/Documentos/Trabajiño AST/Pelsonaje-removebg-preview.png'))
    enemyX.append(random.randint(0.736))
    enemyY.append(random.randint(50.150))
    enemyX_change.append(4)
    enemyY_change.append(40)


#disparo

armaImg= pygame.image.load("/home/pc18/Documentos/Trabajiño AST/Pelsonaje-removebg-preview.png")
armaX=0
armaY=480
armaX_change=0
armaY_change=10
arma_estado="ready"


#porcenteje

score_value=0
font = pygame.font.Font('freesansbold.ttf',64)

textX=10
textY=10


#juego terminado

over_font = pygame.font.Font('freesansbold.ttf',64)

def show_puntaje(x,y):
    score=font.render("score : " +str(score_value),True,255,255,255)
    screen.blit(score,(x,y))
def gemeover_text():
    over_text=over_font.render("Game Over",True,255,255,255)
    screen.blit(over_text,(200,250))
def player (x,y):
    screen.blit(playerImg,(x,y))
def enemy (x,y,i):
    screen.blit(enemyImg[i],(x,y))
def iniciar_disparo (x,y):
    global arma_estado
    arma_estado = "Fire"
    screen.blit(armaImg,(x+16,y+10))
def iscollision (enemyX, enemyY, armaX, armaY):
    distance = math.sqrt(math.pow(enemyX-armaX)+(math.pow(enemyY-armaY,2)))
    if distance<27:
        return True
    else : return.False

#ciclo

running = True
while running:
    screen.fill((0,0,0))
    #imagen del fondo
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #control

            if event.type == pygame.KEYDOWN:
                if playerx_change==pygame.K_LEFT:
                    playerx_change=.5
            if event.key==pygame.K_RIGHT:
                playerx_change=-.5
