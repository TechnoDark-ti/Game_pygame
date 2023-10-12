import pygame
from pygame.locals import *

pygame.init()

screenDimension = (500, 500)
screen = pygame.display.set_mode(screenDimension, 0, 32)

player = pygame.image.load("./assets/player/player.png")
keys =[False, False, False, False]
playerPosition = [200, 300]
velocidade = 10

while True:

    screen.blit(player, playerPosition )
    pygame.display.flip()

    screen.fill(0)  
    pygame.draw.polygon(screen,(0, 255, 0), ( (10, 250), (250, 110,), (500,250), (250, 390), (10, 250) ), 0)
    pygame.draw.line(screen, (170, 150, 0), (9, 270), (250, 410), 42)
    pygame.draw.line(screen, (100, 80, 0), (250, 410), (499, 270), 42)
    
    
    casa = pygame.image.load("./assets/cenário/cenário.png")   
    screen.blit(casa, (180,90) )
    


    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False 

        if keys[0]:
            playerPosition[1] -= velocidade # Movimentar pra cima
        elif keys[1]:
            playerPosition[0] -= velocidade # Movimentar para esquerda
        if keys[2]:
            playerPosition[1] += velocidade # Movimentar para baixo
        elif keys[3]:
            playerPosition[0] += velocidade # movimentar para direita 


        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    
    #pygame.display.update()