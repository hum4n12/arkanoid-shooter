import pygame
from .Shape import Shape

class Circle(Shape):

    def __init__(self, position: pygame.Vector2, radius: int) -> None:
        super().__init__(position)
        self.radius = radius

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.position, self.radius)

    def get_center(self) -> pygame.Vector2:
        return pygame.Vector2(self.position.x, self.position.y)