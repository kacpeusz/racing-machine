import pygame
import settings

class Vehicle:
    car_1 = pygame.image.load("./assets/car_1.png")

    def __init__(self, x, y):
        self.width = settings.VEHICLE_WIDTH
        self.height = settings.VEHICLE_HEIGHT
        self.x = x
        self.y = y
        self.speed = settings.VEHICLE_SPEED

        #self.color = settings.BLUE

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y +=  self.speed

        #self.x = max(0, min(settings.VEHICLE_WIDTH - self.width, self.x))
        #self.y= max(0, min(settings.VEHICLE_HEIGHT - self.height, self.y))

    def draw(self, screen):
        screen.blit(self.car_1, (self.x, self.y))
        #pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
