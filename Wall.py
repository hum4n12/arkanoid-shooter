import pygame

from Entity import Entity
from shapes.Rectangle import Rectangle


class Wall(Entity[Rectangle]):
    color: pygame.Color = (130, 130, 130)

    def __init__(self, shape: Rectangle):
        super().__init__(shape)

    def update(self, dt: float) -> None:
        pass

    def draw(self, surface: pygame.surface) -> None:
        rect = pygame.Rect(self.shape.position.x, self.shape.position.y, self.shape.width, self.shape.height)
        pygame.draw.rect(surface, Wall.color, rect)