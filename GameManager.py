import sys

import pygame

from Level import Level
from Player import Player
from Bullet import Bullet
import Config
from collision_resolvers.CollisionResolver import CollisionResolver
from collision_resolvers.AxisEnum import AxisEnum
from commands.InputHandler import InputHandler
from CollisionDetector import CollisionDetector
from shapes.Rectangle import Rectangle

class GameManager:
    size = (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    def __init__(self):
        self.level = Level(0)
        self.handler: InputHandler = None

    def load(self) -> None:
        self.level.load()
        self.handler = InputHandler(self.level.player, self.level)
        self.handler.init()

    def update(self, clock: pygame.time.Clock) -> None:
        self.input_handler()
        self.level.update(0)

    def draw(self) -> None:
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        pygame.display.flip()

    def input_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.handler.handle_input(event)