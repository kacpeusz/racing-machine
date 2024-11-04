import pygame
import sys
import settings
import vehicle
from pygame.locals import *

from vehicle import Vehicle

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(settings.WINDOW_TITLE)

vehicle = Vehicle(settings.VEHICLE_WIDTH //2, settings.VEHICLE_HEIGHT //2)

while True:

    screen.blit(settings.background, (0, 0))

    vehicle.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    vehicle.handle_movement()

    pygame.display.flip()

pygame.quit()


