from .IEffect import IEffect

class EffectTimer:

    def __init__(self, duration: float, effect: IEffect) -> None:
        self.duration = duration
        self.effect = effect
        self.end: bool = False

    def update(self, dt: float):
        self.duration -= dt
        
        if self.duration <= 0.0:
            self.effect.clean_up()
            self.end = True
            return
        
        self.effect.apply()
        
            
    def is_end(self) -> bool:
        return self.end