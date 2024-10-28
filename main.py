import pygame
import sys


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BG_COLOR = (255, 255, 255)
BOARD_SIZE = 8
TILE_SIZE = SCREEN_WIDTH // BOARD_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("racing-machine")


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 == 0:
                color = (255, 255, 255)
            else:
                color = (0, 0, 0)

            pygame.draw.rect(screen, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.update()

pygame.quit()


