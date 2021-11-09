import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

game_over = False

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

