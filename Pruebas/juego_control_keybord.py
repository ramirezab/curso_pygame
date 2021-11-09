import pygame
import sys
import random
size = (1000, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

pygame.mouse.set_visible(0)
x=0
y=0
vel_x=3
vel_y=3
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos teclado

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x= x -vel_x
            if event.key == pygame.K_RIGHT:
                x= x +vel_x
            if event.key == pygame.K_UP:
                y= x -vel_y
            if event.key == pygame.K_DOWN:
                y= x +vel_y


        if event.type == pygame.KEYUP:
            pass
    if x < 0:
        x=0
    if x > 800:
        x=800
    screen.fill((255, 255, 255))

    

    pygame.draw.rect(screen, (0,0,0), (x, y, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)