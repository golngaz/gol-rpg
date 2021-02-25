import pygame
from pygame.rect import Rect

from src.Game.Sprite import Sprite


class Tileset:
    def __init__(self, file: str, sprite_width: int, sprite_height: int, width: int, height: int):
        if width % sprite_width != 0 or height % sprite_height != 0:
            raise Exception('Tileset is not cuttable : {} by {} sprite for {} by {} tileset'
                            .format(sprite_width, sprite_height, width, height))

        self._image = None
        self._file = file
        self._sprite_width = sprite_width
        self._sprite_height = sprite_height
        self._width = width
        self._height = height

    def load(self):
        self._image = pygame.image.load(self._file).convert_alpha()

    def sprite(self, x: int, y: int) -> Sprite:
        """
        :param x: x sprite coord
        :param y: y sprite coord
        """
        return Sprite(
            self._image,
            Rect(x * self._sprite_width, y * self._sprite_height, self._sprite_width, self._sprite_height)
        )

    def __str__(self):
        return '{}:({},{},{},{})'.format(self._file, self._sprite_width, self._sprite_height, self._width, self._height)
