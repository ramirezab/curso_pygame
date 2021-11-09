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

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((255, 255, 255))

    mouse_pos=pygame.mouse.get_pos()

    pygame.draw.rect(screen, (0,0,0), (mouse_pos[0], mouse_pos[1], 50, 50))
    pygame.display.flip()
    clock.tick(60)