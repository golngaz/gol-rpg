from __future__ import annotations

from pygame.surface import Surface

from src.Game import SpriteMap


class Layer:
    def __init__(self, sprites: list = []):
        self._sprites = sprites

    def add_sprite(self, sprite: SpriteMap) -> Layer:
        self._sprites.append(sprite)

        return self

    def load(self):
        for sprite in self._sprites:
            sprite.load()

    def draw(self, surface: Surface):
        for sprite in self._sprites:
            sprite.draw(surface)

    def __str__(self) -> str:
        to_return = '[\n'

        for i, sprite in enumerate(self._sprites):
            to_return += '{}:{}\n'.format(i, sprite)

        return to_return + ']'
