import pygame
from MapData import MapData
from MapParser import MapParser
from Bullet import Bullet
from Player import Player
from CollisionDetector import CollisionDetector
from collision_resolvers.CollisionResolver import CollisionResolver
from collision_resolvers.AxisEnum import AxisEnum
from shapes.Rectangle import Rectangle
from enemies.Enemy import Enemy
from enemies.EnemyFactory import EnemyFactory
from pathfinding.AStarFinder import AStarFinder
from utils.Timer import Timer

class Level:
    def __init__(self, level: int, font):
        self.font = font
        self.map_parser: MapParser = MapParser()
        self.level: int = level
        self.map_data: MapData = None
        self.enemy_factory: EnemyFactory = EnemyFactory()
        self.player: Player = None
        self.bullets: list[Bullet] = []
        self.enemies: list[Enemy] = []
        self.collision_detector: CollisionDetector = None
        self.collision_resolver: CollisionResolver = None
        self.path_finder: AStarFinder = None
        self.finding_path_timer: Timer = Timer(1.0, self.find_path)

    def find_path(self, enemy: Enemy) -> None:
        found_path = self.path_finder.find_path(MapParser.calculate_tile_from_position(enemy.shape.get_center()), MapParser.calculate_tile_from_position(self.player.shape.get_center()), self.map_data.map)
        path = []
        for p in found_path:
            x = p[0] * MapParser.TILE_SIZE + MapParser.TILE_SIZE // 2
            y = p[1] * MapParser.TILE_SIZE + MapParser.TILE_SIZE // 2
            path.append((x, y))
        enemy.set_path(path)

    def load(self) -> None:
        self.map_data = self.map_parser.load_map(self.level)
        self.player = self.create_player()
        self.enemies.append(self.enemy_factory.create_example_enemy(pygame.Vector2(80, 80),self.player))
        self.collision_detector = CollisionDetector()
        self.collision_resolver = CollisionResolver()
        self.path_finder = AStarFinder()

    def update(self, dt: float) -> None:
        self.player.update(dt)
        self.player.apply_effects(dt)
        for enemy in self.enemies:
            enemy.update(dt)
            enemy.apply_effects(dt)
            self.finding_path_timer.update(dt, enemy)

        for bullet in self.bullets:
            bullet.update(dt)
            bullet.apply_effects(dt)
        
        self.resolve_collisions(dt)
        self.clear()

    def draw(self, surface) -> None:
        for wall in self.map_data.walls:
            wall.draw(surface)

        self.player.draw(surface)

        for bullet in self.bullets:
            bullet.draw(surface)

        for enemy in self.enemies:
            enemy.draw(surface)

    def create_player(self) -> Player:
        shape = Rectangle(self.map_data.player_position, Player.SIZE, Player.SIZE)
        return Player(shape)
    
    def resolve_collisions(self, dt: float) -> None:
        self.player.move_x(Player.SPEED * dt)
        for bullet in self.bullets:
            bullet.shape.set_color((0, 0, 255))
            bullet.move(Bullet.SPEED * dt)
        
        for enemy in self.enemies:
            enemy.move_x(Enemy.SPEED * dt)

        for wall in self.map_data.walls:
            if self.collision_detector.detect_collision(wall.shape, self.player.shape):
                self.collision_resolver.wall_resolve(wall, self.player, AxisEnum.X_AXIS)
            for enemy in self.enemies:
                if self.collision_detector.detect_collision(wall.shape, enemy.shape):
                    self.collision_resolver.wall_resolve(wall, enemy, AxisEnum.X_AXIS)
        
        for bullet in self.bullets:
            for wall in self.map_data.walls:
                if self.collision_detector.detect_collision(wall.shape, bullet.shape):
                    self.collision_resolver.bouncy_bullet_wall_resolve(bullet, wall)
            if bullet.is_hit:
                bullet.shape.set_direction(bullet.shape.direction.reflect(bullet.reflect_vector.normalize()))
        
        for bullet in self.bullets:
            bullet.is_hit = False
            for enemy in self.enemies:
                if self.collision_detector.detect_collision(bullet.shape, enemy.shape):
                    self.collision_resolver.hit_enemy_collision(enemy, bullet)
                    
        
        self.player.move_y(Player.SPEED * dt)
        for enemy in self.enemies:
            enemy.move_y(Enemy.SPEED * dt)
        for wall in self.map_data.walls:
            if self.collision_detector.detect_collision(wall.shape, self.player.shape):
                self.collision_resolver.wall_resolve(wall, self.player, AxisEnum.Y_AXIS)
            
            for enemy in self.enemies:
                if self.collision_detector.detect_collision(wall.shape, enemy.shape):
                    self.collision_resolver.wall_resolve(wall, enemy, AxisEnum.Y_AXIS)

    def clear(self) -> None:
        for index, bullet in enumerate(self.bullets):
            if bullet.is_outside_screen() or bullet.is_destroyed:
                self.bullets.pop(index)
        
        for index, enemy in enumerate(self.enemies):
            if not enemy.is_alive:
                self.enemies.pop(index)
                continue