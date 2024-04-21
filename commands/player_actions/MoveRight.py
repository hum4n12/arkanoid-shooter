import pygame

from Config import KEY_BINDINGS
from Entity import Entity
from Level import Level
from commands.ActionsEnum import ActionsEnum
from commands.Binding import Binding
from commands.IAction import IAction


class MoveRight(IAction):

    def __init__(self, entity: Entity, level: Level, key_bindings: dict[int, list[Binding]]):
        super().__init__(entity, level, key_bindings)

    def register_bindings(self):
        self.register_binding(pygame.KEYDOWN, ActionsEnum.MOVE_RIGHT.value, self.key_down)
        self.register_binding(pygame.KEYUP, ActionsEnum.MOVE_RIGHT.value, self.key_up)

    def key_down(self):
        self.entity.shape.direction.x = 1

    def key_up(self):
        if pygame.key.get_pressed()[KEY_BINDINGS[ActionsEnum.MOVE_LEFT.value]]:
            self.entity.shape.direction.x = -1
        else:
            self.entity.shape.direction.x = 0
