import pygame

from Entity import Entity
from shapes.Shape import Shape
from .attack_patterns.AttackPattern import AttackPattern

class Enemy(Entity):
    def __init__(self, shape: Shape, attack_pattern: AttackPattern) -> None:
        super().__init__(shape)
        self.attack_pattern = attack_pattern

    def update(self, dt: float) -> None:
        self.attack_pattern.attack()