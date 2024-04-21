from MapData import MapData
from MapParser import MapParser
from Bullet import Bullet
from Player import Player
from CollisionDetector import CollisionDetector
from collision_resolvers.CollisionResolver import CollisionResolver
from collision_resolvers.AxisEnum import AxisEnum
from shapes.Rectangle import Rectangle

class Level:
    def __init__(self, level: int):
        self.map_parser: MapParser = MapParser()
        self.level: int = level
        self.map_data: MapData = MapData()
        self.player: Player = None
        self.bullets: list[Bullet] = []
        self.collision_detector: CollisionDetector = None
        self.collision_resolver: CollisionResolver = None

    def load(self) -> None:
        self.map_data = self.map_parser.load_map(self.level)
        self.player = self.create_player()
        self.collision_detector = CollisionDetector()
        self.collision_resolver = CollisionResolver()

    def update(self, dt: float) -> None:
        self.player.update(0)
        for bullet in self.bullets:
            bullet.update(0)
        self.resolve_collisions()
        self.clear()

    def draw(self, surface) -> None:
        for wall in self.map_data.level_map:
            wall.draw(surface)

        self.player.draw(surface)

        for bullet in self.bullets:
            bullet.draw(surface)

    def create_player(self) -> Player:
        shape = Rectangle(self.map_data.player_position, Player.SIZE, Player.SIZE)
        return Player(shape)
    
    def resolve_collisions(self) -> None:
        self.player.move_x(Player.SPEED)
        for bullet in self.bullets:
            bullet.shape.set_color((0, 0, 255))
            bullet.move(Bullet.SPEED)

        for wall in self.map_data.level_map :
            if self.collision_detector.detect_collision(wall.shape, self.player.shape):
                self.collision_resolver.wall_resolve(wall, self.player, AxisEnum.X_AXIS)
            for bullet in self.bullets:
                if self.collision_detector.detect_collision(wall.shape, bullet.shape):
                    self.collision_resolver.bouncy_bullet_wall_resolve(bullet, wall, AxisEnum.X_AXIS)
        
        self.player.move_y(Player.SPEED)
        for wall in self.map_data.level_map:
            if self.collision_detector.detect_collision(wall.shape, self.player.shape):
                self.collision_resolver.wall_resolve(wall, self.player, AxisEnum.Y_AXIS)

    def clear(self) -> None:
        for index, bullet in enumerate(self.bullets):
            if bullet.is_outside_screen() or bullet.is_destroyed:
                self.bullets.pop(index)