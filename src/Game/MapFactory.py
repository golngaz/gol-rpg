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
        print(os.path.realpath(self._config.get('maps.path', '')))
        file_name = self._config.get('maps.path', '') + map.name() + '.bin'
        file = None

        try:
            file = open(file_name, 'wb+')
            pickle.dump(map, file)
        except FileNotFoundError as e:
            raise FileNotFoundError('failed dump file {}'.format(file_name), e)
        finally:
            if file:
                file.close()

    def map(self, map_name) -> Map:
        if map_name not in self._maps:
            return self._load(map_name)

        return self._maps[map_name]

    def _load(self, map_name: str, replace: bool = False) -> Map:
        file = None
        try:
            file = open(self._config.get('maps.path', '') + map_name + '.bin', 'rb')
        except IOError:
            if file:
                file.close()
            raise Exception('Map not found')

        try:
            map = pickle.load(file)
        finally:
            file.close()

        if not replace and map.name() in self._maps:
            raise Exception('Map already loaded')

        self._maps[map.name()] = map

        return map
