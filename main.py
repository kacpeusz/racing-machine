import sys

import pygame
import settings

from vehicle import Vehicle

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption(settings.WINDOW_TITLE)

vehicle = Vehicle(570, 45, settings.VEHICLE_ROTATION_VELOCITY, settings.VEHICLE_MAX_VELOCITY)

while True:

    screen.blit(settings.background, (0, 0))

    vehicle.draw_vehicle(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    vehicle.handle_movement()

    pygame.display.flip()

pygame.quit()
