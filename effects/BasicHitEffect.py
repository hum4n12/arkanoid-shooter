from Entity import Entity
from .IEffect import IEffect

class BasicHitEffect(IEffect):

    DURATION = 0.2

    def __init__(self, entity: Entity) -> None:
        self.entity = entity
        self.old_color = entity.shape.color

    def apply(self) -> None:
        self.entity.shape.set_color((255, 128, 0))
    
    def clean_up(self) -> None:
        self.entity.shape.set_color(self.old_color)