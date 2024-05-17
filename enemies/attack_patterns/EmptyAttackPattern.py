from Entity import Entity
from .AttackPattern import AttackPattern

class EmptyAttackPattern(AttackPattern):

    def __init__(self, attack_target: Entity) -> None:
        super().__init__(attack_target)
    
    def attack(self, dt: float) -> None:
        pass