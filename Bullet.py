import pygame
import Config

from Entity import Entity
from shapes.Circle import Circle

class Bullet(Entity[Circle]):
    SIZE = 10
    SPEED = 600

    def __init__(self, position: pygame.Vector2):
        super().__init__(Circle(position, Bullet.SIZE))
        self.bounces = 10
        self.is_destroyed = False
        self.shape.color = (0, 0, 255)
        self.is_hit: bool = False
        self.reflect_vector: pygame.Vector2 = pygame.Vector2(0, 0)

    def update(self, dt: float):
        pass

    def collide(self) -> None:
        if self.bounces == 0:
            self.is_destroyed = True
        else:
            self.bounces -= 1

    def is_outside_screen(self) -> bool:
        return (self.shape.position.x > Config.SCREEN_WIDTH or self.shape.position.x < 0) or (self.shape.position.y > Config.SCREEN_HEIGHT or self.shape.position.y < 0)
