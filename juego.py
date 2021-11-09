import pygame
import sys

pygame.init()

GREEN=(0, 255, 0)

# Tamañ de pantalla
size = (800, 500)

screen= pygame.display.set_mode(size)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255 ,255 ,255))
    ### --------- Zona de dibujo

    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 8)
    pygame.draw.rect(screen, GREEN, (125, 200, 375, 600), 10)

    ### --------- Zona de dibujo

    pygame.display.flip()