from abc import ABC, abstractmethod

from Player import Player
from commands.Binding import Binding


class IAction(ABC):

    def __init__(self, player: Player, key_bindings: dict[int, list[Binding]]) -> None:
        self.player = player
        self.key_bindings: dict[int, list[Binding]] = key_bindings

    @abstractmethod
    def register_bindings(self) -> None:
        pass

    def register_binding(self, event_type: int, action: int, command: callable):
        if event_type not in self.key_bindings:
            self.key_bindings[event_type] = []

        self.key_bindings[event_type].append(Binding(action, command))
