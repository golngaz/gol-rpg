from abc import ABC, abstractmethod

import pygame
from pygame import Rect

from src.Core import Core
from src.Game.Sprite import Sprite
from src.Menu.AbstractElement import AbstractElement


class Button(AbstractElement, ABC):

    def __init__(self, rect: Rect, file: str):
        super().__init__(rect)

        self._file = file
        self._image = None
        self._sprite_active = None
        self._sprite_inactive = None

    def load(self):
        self._image = pygame.image.load(self._file).convert_alpha()
        self._init_sprites()

    @abstractmethod
    def _init_sprites(self): ...

    def draw(self, surface: pygame.Surface):
        if self._hold:
            self._sprite_active.draw(surface, (self.rect().x, self.rect().y))
        else:
            self._sprite_inactive.draw(surface, (self.rect().x, self.rect().y))

        return self

    def on_click(self, x: float, y: float, core: Core): ...
