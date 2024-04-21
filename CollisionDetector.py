import pygame

from shapes.Shape import Shape
from shapes.Rectangle import Rectangle
from shapes.Circle import Circle

class CollisionDetector:

    def __init__(self) -> None:
        pass

    def detect_collision(self, first: Shape, second: Shape) -> bool:
        if isinstance(first, Rectangle) and isinstance(second, Rectangle):
            return self.rect_rect(first, second)
        elif isinstance(first, Rectangle) and isinstance(second, Circle):
            return self.rect_circle(first, second)
        elif isinstance(first, Circle) and isinstance(second, Rectangle):
            return self.rect_circle(second, first)
        elif isinstance(first, Circle) and isinstance(second, Circle):
            return self.circle_circle(first, second)
        else:
            raise ValueError("Unsupported collision types")
        
    def rect_rect(self, r1: Rectangle, r2: Rectangle) -> bool:
        return r1.position.x < r2.position.x + r2.width and r1.position.x + r1.width > r2.position.x and r1.position.y < r2.position.y + r2.height and r1.position.y + r1.height > r2.position.y
    
    def rect_circle(self, rect: Rectangle, circle: Circle) -> bool:
        nearest_point = CollisionDetector.calculate_rect_circle_nearest_point(rect, circle)
        return nearest_point.distance_to(circle.position) < circle.radius

    def circle_circle(self, c1: Circle, c2: Circle) -> bool:
        return c1.position.distance_to(c2) < c1.radius + c2.radius

    @staticmethod
    def calculate_rect_circle_nearest_point(rect: Rectangle, circle: Circle) -> pygame.Vector2:
        nx = CollisionDetector.clamp(rect.position.x, rect.position.x + rect.width, circle.position.x)
        ny = CollisionDetector.clamp(rect.position.y, rect.position.y + rect.height, circle.position.y)
        return pygame.Vector2(nx, ny)

    @staticmethod    
    def clamp(min_val: float, max_val: float, n: float) -> float:
        return max(min_val, min(max_val, n))
