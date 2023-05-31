import pygame

from GameManager import GameManager


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_manager: GameManager = GameManager()

    game_manager.load()
    
    while True:
        game_manager.update(clock)
        game_manager.draw()
        clock.tick(60)


if __name__ == "__main__":
    main()
