import pygame

from Config import KEY_BINDINGS
from Player import Player
from commands.ActionsEnum import ActionsEnum
from commands.Binding import Binding
from commands.IAction import IAction


class MoveLeft(IAction):

    def __init__(self, player: Player, key_bindings: dict[int, list[Binding]]):
        super().__init__(player, key_bindings)

    def register_bindings(self):
        self.register_binding(pygame.KEYDOWN, ActionsEnum.MOVE_LEFT.value, self.key_down)
        self.register_binding(pygame.KEYUP, ActionsEnum.MOVE_LEFT.value, self.key_up)

    def key_down(self):
        self.player.direction.x = -1

    def key_up(self):
        if pygame.key.get_pressed()[KEY_BINDINGS[ActionsEnum.MOVE_RIGHT.value]]:
            self.player.direction.x = 1
        else:
            self.player.direction.x = 0
