import pygame
import sys


pygame.init()

GREEN=(0, 255, 0)
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)

# Tamañ de pantalla
size = (1000, 800)

screen= pygame.display.set_mode(size)

coordenada_x=100
coordenada_y=100
velocidad_x =3
velocidad_y =3


# Bucle principal
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    ### ------Logica
    if coordenada_x >1000 or coordenada_x < 0:

        velocidad_x *= -1
    
    if event.type == pygame.KEYDOWN:
        coordenada_x=coordenada_x+velocidad_x

     ### ------Logica

    screen.fill((255 ,255 ,255))
    ### --------- Zona de dibujo

    pygame.draw.rect(screen, RED, (coordenada_x, coordenada_y, 50, 50))
    

    ### --------- Zona de dibujo

    pygame.display.flip()