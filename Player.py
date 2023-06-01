import pygame
import math

from Entity import Entity
from Bullet import Bullet


class Player(Entity):
    width: int = 50
    height: int = 50
    speed: int = 10

    def __init__(self, position: pygame.Vector2 = pygame.Vector2(0, 0)):
        super().__init__(position, Player.speed)
        self.shape = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.bullets = []

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, (255, 0, 0), self.shape)
