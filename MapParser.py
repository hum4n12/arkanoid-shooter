import csv
import pygame

from MapData import MapData
from Wall import Wall
from shapes.Rectangle import Rectangle


class MapParser:
    MAPS_PATH: str = "maps"
    PLAYER_NUMBER: int = 2136
    TILE_SIZE: int = 64

    def load_map(self, map_number: int) -> MapData:
        map_number_str: str = str(map_number)
        map: dict[tuple[int, int], int] = {}

        with open(f"{self.MAPS_PATH}/{map_number_str}/{map_number_str}.csv", "r") as file:
            csv_reader = csv.reader(file, delimiter=',')
            for y, row in enumerate(csv_reader):
                for x, value in enumerate(row):
                    map[(x, y)] = int(value)

        return self.generate_rect_map(map)

    def generate_rect_map(self, raw_map: dict[tuple[int, int], int]) -> MapData:
        map_data: MapData = MapData(raw_map)
        x: int = 0
        y: int = 0

        for position, value in raw_map.items():
            x, y = position
            x *= MapParser.TILE_SIZE
            y *= MapParser.TILE_SIZE
            if value == self.PLAYER_NUMBER:
                map_data.player_position = pygame.Vector2(x, y)
            elif value == 0:
                map_data.walls.append(Wall(Rectangle(pygame.Vector2(x, y), MapParser.TILE_SIZE, MapParser.TILE_SIZE)))

        return map_data

    @staticmethod
    def calculate_tile_from_position(position: pygame.Vector2) -> tuple[int, int]:
        return (position.x // MapParser.TILE_SIZE, position.y // MapParser.TILE_SIZE)
