import pygame
import sys

pygame.init()

GREEN=(0, 255, 0)

# Tamañ de pantalla
size = (1000, 800)

screen= pygame.display.set_mode(size)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255 ,255 ,255))
    ### --------- Zona de dibujo

    for x in range(100, 700, 10):

        pygame.draw.rect(screen, GREEN, (x, 200, 50, 50))
        pygame.draw.line(screen, (0,0,0), (x, 0), (100, x), 5)

    ### --------- Zona de dibujo

    pygame.display.flip()