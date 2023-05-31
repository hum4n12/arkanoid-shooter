import pygame
from Entity import Entity
import Config

class Bullet(Entity):
    speed = 12

    def __init__(self, position: pygame.Vector2 = pygame.Vector2(0, 0)):
        super().__init__(position, Bullet.speed)
        # self.radius = 12
        self.width = 10
        self.height = 10
        self.shape = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        self.bounces = 10
        self.is_destroyed = False

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, (0, 0, 255), pygame.Vector2(self.shape.centerx, self.shape.centery), self.width - 3)
        # pygame.draw.rect(surface, (255, 0, 0), self.shape)

    def update(self):
        # self.move()
        pass

    def collide(self) -> None:
        if self.bounces == 0:
            self.is_destroyed = True
        else:
            self.bounces -= 1

    def is_outside_screen(self) -> bool:
        return (self.position.x > Config.screen_width or self.position.x < 0) or (self.position.y > Config.screen_height or self.position.y < 0)
