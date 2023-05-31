import pygame
from pygame import Vector2

from Entity import Entity

class Wall(Entity):
    pos: Vector2 = Vector2(0, 0)
    width: int = None
    height: int = None
    shape = None
    color: pygame.Color = (130, 130, 130)

    def __init__(self, position: Vector2, width: int, height: int):
        super().__init__(position)
        self.width = width
        self.height = height
        self.shape = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def update(self, offset: Vector2):
        self.pos += offset

    def draw(self, surface: pygame.surface):
        self.shape.x, self.shape.y = self.position
        pygame.draw.rect(surface, Wall.color, self.shape)

    def collide(self, x: int, y: int):
        return (x >= self.position.x and x <= self.position.x + self.width) and(y >= self.position.y and y <= self.position.y + self.height)