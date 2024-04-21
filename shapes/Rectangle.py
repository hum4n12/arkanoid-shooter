import pygame
from .Shape import Shape

class Rectangle(Shape):
    
    def __init__(self, position: pygame.Vector2, width: int, height: int) -> None:
        super().__init__(position)
        self.width = width
        self.height = height

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)

    def get_center(self) -> pygame.Vector2:
        return pygame.Vector2(self.position.x + (self.width / 2), self.position.y + (self.height / 2))
    