from pygame import Surface
from abc import ABC, abstractmethod
from shapes.Shape import Shape
from typing import TypeVar, Generic
from effects.EffectTimer import EffectTimer

ShapeT = TypeVar('ShapeT', bound='Shape')

class Entity(ABC, Generic[ShapeT]):
    
    def __init__(self, shape: ShapeT) -> None:
        self.shape: Shape = shape
        self.effects: list[EffectTimer] = []
        self.dt = 0.0 

    @abstractmethod
    def update(self, dt: float) -> None:
        pass
    
    def apply_effects(self, dt: float) -> None:
        self.effects = [effect for effect in self.effects if not effect.is_end()]
        
        for effect in self.effects:
            effect.update(dt)

    def add_effect(self, effect: EffectTimer) -> None:
        self.effects.append(effect)
    
    # is meant to be overwritten in derived classes
    def draw(self, surface: Surface) -> None:
        self.shape.draw(surface)

    def move_x(self, speed: float) -> None:
        self.shape.move_x(speed)

    def move_y(self, speed: float) -> None:
        self.shape.move_y(speed)
    
    def move(self, speed: float) -> None:
        self.shape.move(speed)
    