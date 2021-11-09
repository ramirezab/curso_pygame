import pygame
import sys
import random
size = (1000, 800)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

coord_list = []
for i in range(100):
        x = random.randint(0, 1000)
        y = random.randint(0, 800)
        coord_list.append([x,y])

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

    

        

    screen.fill((255, 255, 255))

    for coord in coord_list:
        
        pygame.draw.circle(screen, (0,0,0), (coord[0], coord[1]), 2)
        coord[1] += 1
        if coord[1] == 800:
            coord[1] = 0
            coord[0] = random.randint(0, 1000)

    pygame.display.flip()
    clock.tick(60)