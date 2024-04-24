import sys

import pygame

from Level import Level
import Config
from commands.InputHandler import InputHandler

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

    def update(self, dt: float) -> None:
        self.input_handler()
        self.level.update(dt)

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