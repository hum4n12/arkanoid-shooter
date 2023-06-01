import math

import pygame

from Bullet import Bullet
from Player import Player
from commands.ActionsEnum import ActionsEnum
from commands.Binding import Binding
from commands.IAction import IAction


class Shoot(IAction):

    def __init__(self, player: Player, key_bindings: dict[int, list[Binding]]):
        super().__init__(player, key_bindings)

    def register_bindings(self):
        self.register_binding(pygame.MOUSEBUTTONDOWN, ActionsEnum.SHOOT.value, self.shoot)

    def shoot(self):
        bullet = Bullet(pygame.Vector2(self.player.shape.centerx, self.player.shape.centery))
        x, y = pygame.mouse.get_pos()
        angle = math.atan2(y - self.player.shape.centery, x - self.player.shape.centerx)
        bullet.set_direction(pygame.Vector2(math.cos(angle), math.sin(angle)))
        self.player.bullets.append(bullet)
