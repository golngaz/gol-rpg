from __future__ import annotations
from src.Config.ConfigInterface import ConfigInterface


class Config(ConfigInterface):
    def __init__(self, data: dict = {}):
        self._data = data

    def get(self, key: str, default=None):
        result = self._data.get(key)

        if not result:
            return default

        return result

    def set(self, key: str, value) -> Config:
        self._data[key] = value

        return self
