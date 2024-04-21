from abc import ABC, abstractmethod

from Entity import Entity
from commands.Binding import Binding
from Level import Level

class IAction(ABC):

    def __init__(self, entity: Entity, level: Level, key_bindings: dict[int, list[Binding]]) -> None:
        self.entity = entity
        self.level = level
        self.key_bindings: dict[int, list[Binding]] = key_bindings

    @abstractmethod
    def register_bindings(self) -> None:
        pass

    def register_binding(self, event_type: int, action: int, command: callable):
        if event_type not in self.key_bindings:
            self.key_bindings[event_type] = []

        self.key_bindings[event_type].append(Binding(action, command))
