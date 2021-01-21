from ctypes import Union

from pygame import Surface

from src.Config.ConfigInterface import ConfigInterface
from src.Game.Character import Character
from src.Game.Map import Map


class MapDisplayer:
    def __init__(self, config: ConfigInterface, player: Character):
        self._maps = {}
        self._current_map: Map
        self._sprite_size = config.get('sprite.size')
        self._surface = self._create_surface(8, 6)
        self._player = player

    def map(self, name: str) -> Map:
        if name not in self._maps:
            raise Exception('Map {} unknown'.format(name))

        return self._maps[name]

    def add_map(self, map: Map):
        self._maps[map.name()] = map

    def set_current_map(self, name: str):
        self._current_map = self.map(name)
        self._surface = self._create_surface(*self._current_map.size())

    def load(self):
        self._current_map\
            .add_character(self._player)\
            .load()

    def tick(self, tick):
        self._current_map.tick(tick, self._surface)

    def draw(self, surface: Surface):
        if not self._current_map:
            raise Exception('No current map configured')

        self._current_map.draw(self._surface)
        x = (surface.get_width() - self._surface.get_width()) / 2
        y = (surface.get_height() - self._surface.get_height()) / 2

        surface.blit(self._surface, (x, y))

    def _create_surface(self, sprites_x: int, sprites_y: int) -> Surface:
        return Surface((self._sprite_size * sprites_x, self._sprite_size * sprites_y))
