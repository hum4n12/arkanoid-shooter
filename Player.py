import pygame
import math

from Entity import Entity
from Bullet import Bullet
from shapes.Rectangle import Rectangle

class Player(Entity[Rectangle]):
    SIZE = 50
    SPEED = 10

    def __init__(self, shape: Rectangle):
        super().__init__(shape)

    def update(self, dt: float) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(self.shape.position.x, self.shape.position.y, self.shape.width, self.shape.height)
        pygame.draw.rect(surface, (255, 0, 0), rect)
