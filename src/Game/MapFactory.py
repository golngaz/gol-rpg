from __future__ import annotations

import os
import pickle

from src.Config import ConfigInterface
from src.Game import Map


class MapFactory:
    def __init__(self, config: ConfigInterface):
        self._maps = {}
        self._config = config

    def save(self, map: Map):
        file_name = self._config.get('maps.path', '') + os.path.sep + map.name() + '.bin'
        file = None

        try:
            file = open(file_name, 'wb+')
            pickle.dump(map, file)
        except FileNotFoundError as e:
            raise FileNotFoundError('failed dump file {}'.format(file_name), e)
        finally:
            if file:
                file.close()

    def map(self, map_name: str) -> Map:
        if map_name not in self._maps:
            return self._load(map_name)

        return self._maps[map_name]

    def _load(self, map_name: str, replace: bool = False) -> Map:
        file = None
        file_path = self._config.get('maps.path', '') + os.path.sep + map_name + '.bin'
        try:
            file = open(file_path, 'rb')
        except IOError:
            if file:
                file.close()
            raise Exception('Map {} not found'.format(file_path))

        try:
            map = pickle.load(file)
        finally:
            file.close()

        if not replace and map.name() in self._maps:
            raise Exception('Map already loaded')

        self._maps[map.name()] = map

        return map
