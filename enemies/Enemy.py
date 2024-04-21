import pygame

from Entity import Entity

class Enemy(Entity):
    def __init__(self, position: pygame.Vector2 = ..., speed: float = 0):
        super().__init__(position, speed)
        # to be remove
        self.width = 40
        self.height = 40
        self.shape = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
