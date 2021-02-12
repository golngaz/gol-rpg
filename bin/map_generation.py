import os
from random import randint

from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Game.Layer import Layer
from src.Game.Map import Map
from src.Game.MapFactory import MapFactory
from src.Game.SpriteMap import SpriteMap
from src.Game.Tileset import Tileset

config = ConfigParserFacade('conf.ini', 'dev', root_directory='..')


def get_tileset_2() -> Tileset:
    file = config.get('tileset.path') + os.path.sep + 'Tileset_48x48_9.png'
    return Tileset(file, 48, 48, 480, 480)


if __name__ == '__main__':
    map = Map('start-map')
    map.set_size((20, 15))

    tileset = get_tileset_2()

    sprites = []
    for x in range(map.size()[0]):
        for y in range(map.size()[1]):
            sprites.append(SpriteMap(
                (x, y),
                (2, 4),
                # (randint(0, 48), randint(0, 48)),
                tileset
            ))

    layer = Layer(sprites)

    map.add_layer(layer)

    factory = MapFactory(config)

    factory.save(map)
