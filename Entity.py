from pygame import Surface
from abc import ABC, abstractmethod
from shapes.Shape import Shape
from typing import TypeVar, Generic

ShapeT = TypeVar('ShapeT', bound='Shape')

class Entity(ABC, Generic[ShapeT]):
    
    def __init__(self, shape: ShapeT) -> None:
        self.shape = shape

    @abstractmethod
    def update(self, dt: float) -> None:
        pass
    
    # is meant to be overwritten in derived classes
    def draw(self, surface: Surface) -> None:
        self.shape.draw(surface)

    def move_x(self, speed: float) -> None:
        self.shape.move_x(speed)

    def move_y(self, speed: float) -> None:
        self.shape.move_y(speed)
    
    def move(self, speed: float) -> None:
        self.shape.move(speed)