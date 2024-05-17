from abc import ABC, abstractmethod
from Entity import Entity

class AttackPattern(ABC):

    def __init__(self, attack_target: Entity) -> None:
        self.attack_target = attack_target

    @abstractmethod
    def attack(self, dt: float) -> None:
        pass