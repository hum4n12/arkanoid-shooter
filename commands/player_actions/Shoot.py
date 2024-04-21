import math

import pygame

from Bullet import Bullet
from Entity import Entity
from Level import Level
from commands.ActionsEnum import ActionsEnum
from commands.Binding import Binding
from commands.IAction import IAction


class Shoot(IAction):

    def __init__(self, entity: Entity, level: Level, key_bindings: dict[int, list[Binding]]):
        super().__init__(entity, level, key_bindings)

    def register_bindings(self):
        self.register_binding(pygame.MOUSEBUTTONDOWN, ActionsEnum.SHOOT.value, self.shoot)

    def shoot(self):
        center_pos = self.entity.shape.get_center()
        bullet = Bullet(pygame.Vector2(center_pos.x, center_pos.y))
        x, y = pygame.mouse.get_pos()
        angle = math.atan2(y - center_pos.y, x - center_pos.x)
        bullet.shape.set_direction(pygame.Vector2(math.cos(angle), math.sin(angle)))
        self.level.bullets.append(bullet)
