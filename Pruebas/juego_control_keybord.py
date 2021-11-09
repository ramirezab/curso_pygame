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
vel_x=0
vel_y=0
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Eventos teclado

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x= -3
            if event.key == pygame.K_RIGHT:
                vel_x= 3
            if event.key == pygame.K_UP:
                vel_y= -3
            if event.key == pygame.K_DOWN:
                vel_y= 3
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vel_x= 0
            if event.key == pygame.K_RIGHT:
                vel_x= 0
            if event.key == pygame.K_UP:
                vel_y= 0
            if event.key == pygame.K_DOWN:
                vel_y= 0
        


        if event.type == pygame.KEYUP:
            pass
    if x < 0:
        x=0
    if x > 800:
        x=800
    if y > 1000:
        y=1000
    if y < 0:
        y=0
    screen.fill((255, 255, 255))

    x += vel_x
    y += vel_y

    pygame.draw.rect(screen, (0,0,0), (x, y, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)