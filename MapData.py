import pygame

from Wall import Wall


class MapData:

    def __init__(self, level_map: list[Wall] = None, player_position: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.level_map: list[Wall] = level_map if level_map is not None else []
        self.player_position: pygame.Vector2 = player_position
