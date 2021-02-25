from pygame.surface import Surface

from src.Game import Tileset


class SpriteMap:
    """
    représente un sprite sur une map en fonction d'un tileset
    """

    def __init__(self, coords_on_the_map, coords_on_the_tileset, tileset: Tileset):
        self._coords_on_the_map = coords_on_the_map
        self._coords_on_the_tileset = coords_on_the_tileset
        self._tileset = tileset

    def load(self):
        self._tileset.load()

    def draw(self, surface: Surface):
        self._tileset.sprite(*self._coords_on_the_tileset).draw(surface, (
            # todo, configurer une taille de sprites sur la map ou revoir cette var en px
            self._coords_on_the_map[0] * 48,
            self._coords_on_the_map[1] * 48
        ))

    def __str__(self):
        return '{}:({},{}),({},{})'.format(
            str(self._tileset)[-35:-16],
            self._coords_on_the_map[0],
            self._coords_on_the_map[1],
            self._coords_on_the_tileset[0],
            self._coords_on_the_tileset[1]
        )
