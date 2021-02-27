import pygame
from pygame import Surface
from src.DisplayerInterface import DisplayerInterface
from src.Menu.AbstractElement import AbstractElement


class TilesetDisplayer(DisplayerInterface):
    def __init__(self, file: str = None):
        self._pos = (0, 0)
        self._hidden = False
        self._file = file
        self._image = None

    def set_file(self, file: str):
        self._file = file

    @staticmethod
    def name():
        return 'TilesetDisplayer'

    def load(self) -> None:
        self._image = pygame.image.load(self._file).convert_alpha()

    def tick(self, tick) -> None:
        pass

    def draw(self, surface: Surface) -> None:
        if self._image is not None and not self._hidden:
            surface.blit(self._image, self._pos)

    def set_pos(self, x: float, y: float):
        self._pos = (x, y)

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False
