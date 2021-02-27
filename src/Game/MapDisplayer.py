from pygame import Surface
from src.Config.ConfigInterface import ConfigInterface
from src.DisplayerInterface import DisplayerInterface
from src.Game.Character import Character
from src.Game.Map import Map


class MapDisplayer(DisplayerInterface):
    def __init__(self, config: ConfigInterface):
        self._pull_bottom = False
        self._pull_top = False
        self._pull_right = False
        self._pull_left = False
        self._characters = list()
        self._maps = {}
        self._current_map: Map
        self._sprite_size = config.get('sprite.size')
        self._surface = self._create_surface(8, 6)

    @staticmethod
    def name() -> str:
        return 'MapDisplayer'

    def add_characters(self, character: Character):
        self._characters.append(character)

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
            .set_characters(self._characters)\
            .load()

    def tick(self, tick):
        self._current_map.tick(tick, self._surface)

    def draw(self, surface: Surface):
        if not self._current_map:
            raise Exception('No current map configured')

        self._current_map.draw(self._surface)

        surface.blit(self._surface, self._map_position(surface))

    def pull_right(self):
        self._pull_right = True
        self._pull_left = False

    def pull_left(self):
        self._pull_right = False
        self._pull_left = True

    def pull_top(self):
        self._pull_bottom = False
        self._pull_top = True

    def pull_bottom(self):
        self._pull_bottom = True
        self._pull_top = False

    def _map_position(self, surface) -> tuple:
        if self._pull_left:
            x = 0
        elif self._pull_right:
            x = surface.get_width() - self._surface.get_width()
        else:
            x = (surface.get_width() - self._surface.get_width()) / 2

        if self._pull_top:
            y = 0
        elif self._pull_bottom:
            y = surface.get_height() - self._surface.get_height()
        else:
            y = (surface.get_height() - self._surface.get_height()) / 2

        return x, y

    def _create_surface(self, sprites_x: int, sprites_y: int) -> Surface:
        return Surface((self._sprite_size * sprites_x, self._sprite_size * sprites_y))
