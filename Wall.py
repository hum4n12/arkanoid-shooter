import pygame

from Entity import Entity
from shapes.Rectangle import Rectangle


class Wall(Entity[Rectangle]):
    COLOR: pygame.Color = (130, 130, 130)

    def __init__(self, shape: Rectangle):
        super().__init__(shape)
        self.shape.set_color(Wall.COLOR)

    def update(self, dt: float) -> None:
        pass

    def draw(self, surface: pygame.surface) -> None:
        self.shape.draw(surface)