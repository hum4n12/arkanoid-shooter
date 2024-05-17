import pygame

from Entity import Entity
from shapes.Shape import Shape
from .attack_patterns.AttackPattern import AttackPattern
radius = 20
class Enemy(Entity):
    SPEED = 200

    def __init__(self, shape: Shape, attack_pattern: AttackPattern) -> None:
        super().__init__(shape)
        self.original_color: tuple[int, int, int] = (0, 0, 0)
        self.attack_pattern = attack_pattern
        self.hp: int = 4
        self.is_alive: bool = True
        self.path: list[pygame.Vector2] = []
        self.collision_rects: list[pygame.Rect] = []
        self.destination = pygame.Vector2(0,0)

    def set_path(self, path: list[tuple[int, int]]) -> None:
        new_path = []
        for p in path:
            new_path.append(pygame.Vector2(p))
        
        if len(new_path) > 0:
            del new_path[-1]
            
        self.path = new_path
        self.set_collision_rects()
        self.get_direction()

    def set_collision_rects(self) -> None:
        if not self.path:
            return
        
        self.collision_rects = []
        for point in self.path:
            rect = pygame.Rect((point.x - 2, point.y - 2), (4,4))
            self.collision_rects.append(rect)

    def get_direction(self) -> None:
        if self.collision_rects:
            start = pygame.math.Vector2(self.shape.get_center())
            end = pygame.math.Vector2(self.collision_rects[-1].center)
            self.shape.direction = (end - start)
        else:
            self.shape.direction = pygame.math.Vector2(0,0)
            self.path = []

    def check_collisions(self) -> None:
        if self.collision_rects:
            for rect in self.collision_rects:
                if rect.collidepoint(self.shape.get_center()):
                    del self.collision_rects[-1]
                    self.get_direction()
        else:
            self.path = []

    def update(self, dt: float) -> None:
        self.check_collisions()
        self.attack_pattern.attack(dt)

    def draw(self, surface: pygame.Surface) -> None:
        self.shape.draw(surface)
        if len(self.path) >= 2:
            pygame.draw.lines(surface,'#fafafa', False, self.path, 5)