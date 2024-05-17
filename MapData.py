import pygame

from Wall import Wall


class MapData:

    def __init__(self, map: dict[tuple[int, int], int], walls: list[Wall] = None, player_position: pygame.Vector2 = pygame.Vector2(0, 0)):
        self.map: dict[tuple[int, int], int] = map
        self.walls: list[Wall] = walls if walls is not None else []
        self.player_position: pygame.Vector2 = player_position