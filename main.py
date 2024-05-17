import pygame, time

from GameManager import GameManager


def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    previous_time: float = time.time()
    game_manager: GameManager = GameManager(font)

    game_manager.load()

    while True:
        dt: float = time.time() - previous_time
        previous_time = time.time()
        game_manager.update(dt)
        game_manager.draw()


if __name__ == "__main__":
    main()
