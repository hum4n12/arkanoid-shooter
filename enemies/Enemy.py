import pygame

from Entity import Entity
from shapes.Shape import Shape
from .attack_patterns.AttackPattern import AttackPattern

class Enemy(Entity):
    def __init__(self, shape: Shape, attack_pattern: AttackPattern) -> None:
        super().__init__(shape)
        self.original_color: tuple[int, int, int] = (0, 0, 0)
        self.attack_pattern = attack_pattern
        self.hp: int = 1
        self.is_alive: bool = True

    def update(self, dt: float) -> None:
        self.attack_pattern.attack()