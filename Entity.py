import pygame
import math

class Entity:
    def __init__(self, position: pygame.Vector2 = pygame.Vector2(0, 0), speed: float = 0):
        self.position: pygame.Vector2 = pygame.Vector2(position)
        self.direction: pygame.Vector2 = pygame.Vector2(0, 0)
        self.speed = speed

    def set_position(self, position: pygame.Vector2):
        self.position = pygame.Vector2(position)
    
    def set_direction(self, position: pygame.Vector2):
        self.direction = pygame.Vector2(position)

    def move_x(self):
        x = self.direction.x
        y = self.direction.y
        length = math.sqrt(x**2 + y**2)
        if not length == 0:
            self.shape.x += (x / length) * self.speed

    def move_y(self):
        x = self.direction.x
        y = self.direction.y
        length = math.sqrt(x**2 + y**2)
        if not length == 0:
            self.shape.y += (y / length) * self.speed

    def move(self):
        x = self.direction.x
        y = self.direction.y
        length = math.sqrt(x**2 + y**2)
        if not length == 0:
            self.position.x += (x / length) * self.speed
            self.position.y += (y / length) * self.speed