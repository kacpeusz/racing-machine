import math
import pygame
import settings
import utils

class Vehicle:
    car_1 = pygame.image.load("./assets/car_1.png")
    def __init__(self, x, y, rotation_vel, max_vel):
        self.width = settings.VEHICLE_WIDTH
        self.height = settings.VEHICLE_HEIGHT
        self.x = x
        self.y = y
        self.speed = settings.VEHICLE_SPEED
        self.angle = 0
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.acceleration = 0.1
        self.max_vel = max_vel

    def rotate(self, left=False, right=False):
        if left:
            self.angle = self.angle + self.rotation_vel
        elif right:
            self.angle = self.angle - self.rotation_vel

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        moving = True
        if keys[pygame.K_LEFT]:
            self.rotate(left=True)
        if keys[pygame.K_RIGHT]:
            self.rotate(right=True)
        if keys[pygame.K_UP]:
            self.move_forward()
        if moving == False:
            self.reduce_speed()

    def draw_vehicle(self, screen):
        utils.blit_rotate_center(screen, self.car_1, (self.x, self.y), self.angle)

    def move_vehicle(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.y = self.y - vertical
        self.x = self.x - horizontal

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move_vehicle()

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move_vehicle()
