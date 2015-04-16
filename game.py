#put in activation
import math
import random

import pygame
from pygame.locals import *


#Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
textRect = 0
PlayerCoords = [320, 375]
keys = [False, False]
Time = 0
Input = 0

#Load Images
Player = pygame.image.load("/home/pi/MastermanPithon/HowTo/PyGame/resources/images/dude.png")


while True:
    screen.fill((0,0,0))
    Time = Time+1
    font = pygame.font.Font(None, 24)
    Timer = font.render(str(Time), True, (255,255,255))
    textRect = Timer.get_rect()
    playerRect = Player.get_rect()
    playerRect.topright =[(PlayerCoords[0]+46), PlayerCoords[1]]
    playerRect.topleft = [(PlayerCoords[0]), PlayerCoords[1]]
    textRect.topright =[635,5]
    screen.blit(Timer, textRect)
    screen.blit(Player, PlayerCoords)

    print playerRect.topleft
    print playerRect.topright
    #input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key==K_a:
                    keys[0]=True
                if event.key==K_d:
                    keys[1]=True
        if event.type == pygame.KEYUP:
                if event.key==pygame.K_a:
                    keys[0]=False
                if event.key==pygame.K_d:
                    keys[1]=False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    #MOvements
    if keys[0]== True: 
        if playerRect.topleft <= 32:
            PlayerCoords[0]-=5
    if keys[1]== True:
        if playerRect.topright >= 585:
            PlayerCoords[0]+=5
    
    

    #refreshes screen DO NOT DELETE PLS
    pygame.display.flip()


        
    

    
    #draw number as x = (image of number)
    Input == input
