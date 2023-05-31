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

    def input_handler(self, event: pygame.event):
        if event.type == pygame.MOUSEBUTTONUP:
            bullet = Bullet(pygame.Vector2(self.shape.centerx, self.shape.centery))
            x, y = pygame.mouse.get_pos()
            angle = math.atan2(y - self.shape.centery, x - self.shape.centerx)
            bullet.set_direction(pygame.Vector2(math.cos(angle), math.sin(angle)))
            self.bullets.append(bullet)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.direction.x = -1
            if event.key == pygame.K_d:
                self.direction.x = 1
            if event.key == pygame.K_w:
                self.direction.y = -1
            if event.key == pygame.K_s:
                self.direction.y = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.direction.x = 1
                else:
                    self.direction.x = 0
            elif event.key == pygame.K_d:
                if pygame.key.get_pressed()[pygame.K_a]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0
            elif event.key == pygame.K_w:
                if pygame.key.get_pressed()[pygame.K_s]:
                    self.direction.y = 1
                else:
                    self.direction.y = 0
            elif event.key == pygame.K_s:
                if pygame.key.get_pressed()[pygame.K_w]:
                    self.direction.y = -1
                else:
                    self.direction.y = 0
