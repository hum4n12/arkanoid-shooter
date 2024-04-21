import pygame
import math

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, position: pygame.Vector2) -> None:
        self.position = position
        self.direction: pygame.Vector2 = pygame.Vector2(0, 0)
        self.color = (0, 0, 0)

    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        pass

    @abstractmethod
    def get_center(self) -> pygame.Vector2:
        pass

    def set_position(self, position: pygame.Vector2) -> None:
        self.position = pygame.Vector2(position)
    
    def set_direction(self, position: pygame.Vector2) -> None:
        self.direction = pygame.Vector2(position)
    
    def set_color(self, color: tuple[int, int, int]) -> None:
        self.color = color

    def move_x(self, speed: float) -> None:
        x = self.direction.x
        y = self.direction.y
        length = math.sqrt(x**2 + y**2)
        if not length == 0:
            self.position.x += (x / length) * speed

    def move_y(self, speed: float) -> None:
        x = self.direction.x
        y = self.direction.y
        length = math.sqrt(x**2 + y**2)
        if not length == 0:
            self.position.y += (y / length) * speed
            
    def move(self, speed: float) -> None:
        if self.direction.length == 0:
            return
        
        self.position += self.direction.normalize() * speed