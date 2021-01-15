import unittest
from src.Config.ConfigInterface import ConfigInterface
from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Game.Map import Map
from src.Game.MapFactory import MapFactory
from tests.TestCase import TestCase


class MapFactoryTest(TestCase):
    def setUp(self):
        self._config = ConfigParserFacade('../conf.ini', 'test')

    def test_save(self):
        factory = MapFactory(self._config)

        map = Map()
        map._name = 'test_save'

        factory.save(map)

    def test_load(self):
        factory = MapFactory(self._config)

        map = factory.map('test_save')

        print(map)


if __name__ == '__main__':
    unittest.main()
