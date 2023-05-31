import sys

import pygame

from Level import Level
from Player import Player
from Bullet import Bullet
import Config

class GameManager:
    size = (Config.screen_width, Config.screen_height)
    screen = pygame.display.set_mode(size)

    def __init__(self):
        self.level = Level(0)
        self.player = None
        self.bullets: list [Bullet] = []

    def load(self):
        self.level.load()
        self.player = Player(self.level.get_player_position())
        self.player.bullets = self.bullets

    def update(self, clock: pygame.time.Clock):
        self.input_handler()
        self.player.update()
        # self.level.update(self.camera.offset)
        for bullet in self.bullets:
            bullet.update()
        self.resolve_collisions()
        self.clear()
        # self.camera.update()

    def clear(self):
        for index, bullet in enumerate(self.bullets):
            if bullet.is_outside_screen() or bullet.is_destroyed:
                self.bullets.pop(index)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
            
        pygame.display.flip()

    def input_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.player.input_handler(event)

    def resolve_collisions(self):
        self.player.move_x()
        for bullet in self.bullets:
            bullet.move_x()

        for wall in self.level.map:
            if wall.shape.colliderect(self.player.shape):
                if self.player.direction.x < 0:
                    self.player.shape.left = wall.shape.right
                elif self.player.direction.x > 0:
                    self.player.shape.right = wall.shape.left
            for bullet in self.bullets:
                if wall.shape.colliderect(bullet.shape):
                    if bullet.direction.x < 0:
                        bullet.shape.left = wall.shape.right
                    elif bullet.direction.x > 0:
                        bullet.shape.right = wall.shape.left
                    bullet.collide()
                    bullet.direction.x = - bullet.direction.x

        self.player.move_y()
        for bullet in self.bullets:
            bullet.move_y()
        for wall in self.level.map:
            if wall.shape.colliderect(self.player.shape):
                if self.player.direction.y < 0:
                    self.player.shape.top = wall.shape.bottom
                elif self.player.direction.y > 0:
                    self.player.shape.bottom = wall.shape.top
            for bullet in self.bullets:
                if wall.shape.colliderect(bullet.shape):
                    if bullet.direction.y < 0:
                        bullet.shape.top = wall.shape.bottom
                    elif bullet.direction.y > 0:
                        bullet.shape.bottom = wall.shape.top
                    bullet.collide()
                    bullet.direction.y = - bullet.direction.y