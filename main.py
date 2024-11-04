import pygame
import sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1012
SCREEN_HEIGHT = 750
BG_COLOR = (255, 255, 255)
BOARD_SIZE = 8
TILE_SIZE = SCREEN_WIDTH // BOARD_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("racing-machine")
background = pygame.image.load("./models/track.jpg")



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))


    pygame.display.update()

pygame.quit()


