from __future__ import annotations

from pygame import Rect
from pygame.surface import Surface

from src.Game.Character import Character
from src.Game.Layer import Layer

BACKGROUND = (100, 150, 100)


class Map:
    def __init__(self, name: str = 'default'):
        # sprites size
        self._size = (8, 6)
        self._characters = []
        self._layers = []
        self._name = name

    def size(self) -> tuple:
        return self._size

    def name(self) -> str:
        return self._name

    def add_layer(self, layer: Layer) -> Map:
        self._layers.append(layer)

        return self

    def add_character(self, character: Character) -> Map:
        self._characters.append(character)

        return self

    def set_characters(self, characters: list) -> Map:
        self._characters = characters

        return self

    def load(self) -> Map:
        for layer in self._layers:
            layer.load()

        for character in self._characters:
            character.load()

        return self

    def draw(self, surface: Surface) -> Map:
        surface.fill(BACKGROUND)

        for layer in self._layers:
            layer.draw(surface)

        for character in self._characters:
            character.draw(surface)

        return self

    def __str__(self) -> str:
        to_return = ''

        for i, layer in enumerate(self._layers):
            to_return += 'layer {} => {}\n'.format(i, layer)

        return to_return

    def tick(self, tick, surface) -> Map:
        for character in self._characters:
            character.tick(tick, surface)

        return self

    def set_size(self, size: tuple) -> Map:
        self._size = size
