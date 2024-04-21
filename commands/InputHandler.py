import importlib
import inspect
import json
import os
import sys

import pygame

from Config import KEY_BINDINGS
from Entity import Entity
from Level import Level
from .ActionsEnum import ActionsEnum
from .Binding import Binding
from .IAction import IAction

MOUSE: dict[str, int] = {
    "MOUSE_LEFT": 1,
    "MOUSE_MIDDLE": 2,
    "MOUSE_RIGHT": 3
}

KEY_BINDINGS_FILE = "commands/key_bindings.json"
KEY = "key"
PLAYER_ACTIONS = "player_actions"


class InputHandler:

    def __init__(self, entity: Entity, level: Level) -> None:
        self.entity = entity
        self.level = level
        self.event_key_bindings: dict[int, list[Binding]] = {}

    def init(self) -> None:
        self._load_key_bindings()
        self._register_bindings()

    def handle_input(self, event: pygame.Event) -> None:
        if event.type not in self.event_key_bindings:
            return

        bindings: list[Binding] = self.event_key_bindings[event.type]

        for binding in bindings:
            key: int = KEY_BINDINGS[binding.action]
            event_key: int = event.key if hasattr(event, KEY) else event.button
            if event_key == key:
                binding.execute()

    def _load_key_bindings(self) -> None:
        with open(KEY_BINDINGS_FILE, 'r') as file:
            bindings: dict[str, str] = json.load(file)
            for action, key in bindings.items():
                KEY_BINDINGS[ActionsEnum[action].value] = self._get_key_from_character(key)

    def _register_bindings(self) -> None:
        current_dir = os.path.basename(os.path.dirname(__file__))
        folder_path = os.path.join(current_dir, PLAYER_ACTIONS)

        for file in os.listdir(folder_path):
            module_name = os.path.splitext(file)[0]
            module_path = f'{current_dir}.{PLAYER_ACTIONS}.{module_name}'
            module = importlib.import_module(module_path)
            action_classes = inspect.getmembers(module, inspect.isclass)

            for name, action_class in action_classes:
                if not name == module_name:
                    continue
                action: IAction = action_class(self.entity, self.level, self.event_key_bindings)
                action.register_bindings()

    @staticmethod
    def _get_key_from_character(key: str) -> int:
        if key in MOUSE:
            return MOUSE[key]

        try:
            key_code: int = pygame.key.key_code(key)
        except ValueError:
            print("An error occured in configuration file")
            pygame.quit()
            sys.exit()

        return key_code
