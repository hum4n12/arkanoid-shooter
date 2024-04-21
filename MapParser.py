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
        raw_map: list[list[int]] = []

        with open(f"{self.MAPS_PATH}/{map_number_str}/{map_number_str}.csv", "r") as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                raw_map.append([int(x) for x in row])

        return self.generate_rect_map(raw_map)

    def generate_rect_map(self, raw_map: list[list[int]]) -> MapData:
        map_data: MapData = MapData()
        x: int = 0
        y: int = 0

        for row in raw_map:
            for col in row:
                if col != -1:
                    if col == self.PLAYER_NUMBER:
                        map_data.player_position = pygame.Vector2(x, y)
                    else:
                        map_data.level_map.append(Wall(Rectangle(pygame.Vector2(x,y), MapParser.TILE_SIZE, MapParser.TILE_SIZE)))
                x += MapParser.TILE_SIZE
            x = 0
            y += MapParser.TILE_SIZE

        return map_data
