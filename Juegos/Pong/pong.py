import pygame
import math
import random
import time

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

game_over = False

# Tamaños de las paletas

player_width=15
player_height=90


# Coordenadas de jugador 1
x1=5
y1=255

#Coordenadas de jugador 2
x2=770
y2=255

# Velocidades de sprites
vel_y1 = 0
vel_y2 = 0
vel_bola_X = 0
vel_bola_y = 0

# Coordenadas de la bola

bola_x=400
bola_y=300
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            
            # Jugador 1
            if event.key == pygame.K_w:
                vel_y1 = -3
            if event.key == pygame.K_s:
                vel_y1 = 3
            
            # Jugador 2
            if event.key == pygame.K_UP:
                vel_y2 = -3
            if event.key == pygame.K_DOWN:
                vel_y2 = 3

            # Inicio del movimiento de la bola

            if event.key == pygame.K_SPACE:
                bola_x=400
                bola_y=300
                vel_bola_X = random.choice((-4,-3,-2,-1,3,4,))
                vel_bola_y = math.sqrt(4.24**2-vel_bola_X**2)
                

                
        if event.type == pygame.KEYUP:

            # Jugador 1
            if event.key == pygame.K_w:
                vel_y1 = 0
            if event.key == pygame.K_s:
                vel_y1 = 0

            # Jugador 2
            if event.key == pygame.K_UP:
                vel_y2 = 0
            if event.key == pygame.K_DOWN:
                vel_y2 = 0

    ### -----------Logica

    # Limites de movimiento de las paletas
    if y1 > 510:
        y1 = 510
    if y1 < 0:
        y1 = 0
    if y2 > 510:
        y2 = 510
    if y2 < 0:
        y2 = 0

    # Movimiento de las paletas
    y1 += vel_y1
    y2 += vel_y2

    
    
    # CAmbio de direccion de la bola
    if bola_y > 580 or bola_y <20:
        vel_bola_y *= -1

    if bola_x > 800:
        vel_bola_y=0
        vel_bola_X=0
        
        bola_X = 400
        
        bola_y = 300
    
    if bola_x < 0:
        vel_bola_y=0
        vel_bola_X=0
        
        bola_X = 400
        
        bola_y = 300
        
        
    # movimiento de la bola

    bola_x += vel_bola_X
    bola_y += vel_bola_y   

    
    ### -----------Logica

    screen.fill((0, 0, 0))
    
    ### ------------Zona de dibujo

    j1=pygame.draw.rect(screen, (255 ,255 ,255), (x1, y1, player_width, player_height))

    j2=pygame.draw.rect(screen, (255 ,255 ,255), (x2, y2, player_width, player_height))

    bola=pygame.draw.circle(screen, (255,255,255), (bola_x,bola_y), 20)

    ### ------------Zona de dibujo

    # Colisiones

    if bola.colliderect(j1) or bola.colliderect(j2):
        vel_bola_X *= -1
    
    pygame.display.flip()

    clock.tick(60)