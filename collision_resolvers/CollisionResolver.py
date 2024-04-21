import pygame

from .AxisEnum import AxisEnum
from Entity import Entity
from shapes.Rectangle import Rectangle
from shapes.Circle import Circle
from Bullet import Bullet
from CollisionDetector import CollisionDetector

class CollisionResolver:

    @staticmethod
    def wall_resolve(wall: Entity[Rectangle], entity: Entity[Rectangle], axis: AxisEnum) -> None:
        wall_shape: Rectangle = wall.shape
        entity_shape: Rectangle = entity.shape
        if axis == AxisEnum.X_AXIS:
            if entity_shape.direction.x > 0:
                entity_shape.position.x = wall_shape.position.x - entity_shape.width
            elif entity_shape.direction.x < 0:
                entity_shape.position.x = wall_shape.position.x + wall_shape.width
        elif axis == AxisEnum.Y_AXIS:
            if entity_shape.direction.y > 0:
                entity_shape.position.y = wall_shape.position.y - entity_shape.height
            elif entity_shape.direction.y < 0:
                entity_shape.position.y = wall_shape.position.y + wall_shape.height
    
    @staticmethod
    def bouncy_bullet_wall_resolve(bullet: Bullet, wall: Entity[Rectangle]) -> None:
        bullet_shape: Circle = bullet.shape
        wall_shape: Rectangle = wall.shape

        bullet_shape.set_color((0, 255, 0))

        nearest_point = CollisionDetector.calculate_rect_circle_nearest_point(wall_shape, bullet_shape)
        ray_to_nearest = nearest_point - bullet_shape.position

        f_overlap: float = bullet_shape.radius - ray_to_nearest.magnitude()
        bullet_new_position: pygame.Vector2 = bullet_shape.position - ray_to_nearest.normalize() * f_overlap
        
        bullet_shape.set_direction(bullet_shape.direction.reflect(ray_to_nearest.normalize()))
        bullet_shape.set_position(bullet_new_position)

        if bullet.bounces <= 0:
            bullet.is_destroyed = True
        else:
            bullet.bounces -= 1