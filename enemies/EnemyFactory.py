import pygame
from Entity import Entity
from .Enemy import Enemy
from shapes.Rectangle import Rectangle
from .attack_patterns.EmptyAttackPattern import EmptyAttackPattern

class EnemyFactory:

    def create_example_enemy(self, position: pygame.Vector2, attack_target: Entity) -> Enemy:
        size = 40
        shape = Rectangle(position, size, size)
        color = (255, 0, 255)
        shape.set_color(color)
        attack_pattern = EmptyAttackPattern(attack_target)
        enemy = Enemy(shape, attack_pattern)
        enemy.hp = 4
        enemy.original_color = color
        return enemy