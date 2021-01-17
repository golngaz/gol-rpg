from __future__ import annotations

from pygame.surface import Surface

from src.Game.Layer import Layer


class Map:
    def __init__(self, name: str = 'default'):
        self._layers = []
        self._name = name

    def name(self) -> str:
        return self._name

    def add_layer(self, layer: Layer) -> Map:
        self._layers.append(layer)

        return self

    def load(self):
        for layer in self._layers:
            layer.load()

    def draw(self, surface: Surface):
        for layer in self._layers:
            layer.draw(surface)

    def __str__(self) -> str:
        to_return = ''

        for i, layer in enumerate(self._layers):
            to_return += 'layer {} => {}\n'.format(i, layer)

        return to_return
