import pygame
from Entity import Entity
from .Enemy import Enemy
from shapes.Rectangle import Rectangle
from .attack_patterns.EmptyAttackPattern import EmptyAttackPattern

class EnemyFactory:

    def create_example_enemy(self, position: pygame.Vector2, attack_target: Entity) -> Enemy:
        size = 40
        shape = Rectangle(position, size, size)
        shape.set_color((255, 0, 255))
        attack_pattern = EmptyAttackPattern(attack_target)
        return Enemy(shape, attack_pattern)