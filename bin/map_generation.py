import os

from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Game.Layer import Layer
from src.Game.Map import Map
from src.Game.MapFactory import MapFactory
from src.Game.SpriteMap import SpriteMap
from src.Game.Tileset import Tileset

config = ConfigParserFacade('..' + os.path.sep + 'conf.ini', 'dev', root_directory='..')


def get_tileset_2() -> Tileset:
    file = config.get('tileset.path') + os.path.sep + 'Tileset_48x48_2.png'
    return Tileset(file, 48, 48, 480, 480)


if __name__ == '__main__':
    map = Map('start-map')

    tileset = get_tileset_2()

    layer = Layer([
        SpriteMap((0, 0), (0, 0), tileset),
        SpriteMap((1, 1), (1, 1), tileset),
        SpriteMap((2, 2), (2, 2), tileset),
        SpriteMap((3, 3), (3, 3), tileset),
        SpriteMap((4, 4), (4, 4), tileset),
        SpriteMap((5, 5), (5, 5), tileset),
        SpriteMap((6, 6), (6, 6), tileset),
        SpriteMap((7, 7), (7, 7), tileset),
        SpriteMap((8, 8), (8, 8), tileset)
    ])

    map.add_layer(layer)

    factory = MapFactory(config)

    factory.save(map)
