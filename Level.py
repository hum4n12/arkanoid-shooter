import pygame

from MapData import MapData
from MapParser import MapParser
from Wall import Wall


class Level:
    def __init__(self, level: int):
        self.map_parser: MapParser = MapParser()
        self.level: int = level
        self.map_data: MapData = MapData()

    @property
    def map(self):
        return self.map_data.level_map 

    def load(self) -> None:
        self.map_data = self.map_parser.load_map(self.level)

    def update(self, offset: pygame.Vector2) -> None:
        for wall in self.map_data.level_map:
            wall.update(offset)

    def draw(self, surface) -> None:
        for wall in self.map_data.level_map:
            wall.draw(surface)

    def get_player_position(self) -> pygame.Vector2:
        return self.map_data.player_position
