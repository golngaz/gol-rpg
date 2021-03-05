from __future__ import annotations

import os
from os.path import realpath
from configparser import ConfigParser, NoOptionError

from src.Config.ConfigInterface import ConfigInterface


class ConfigParserFacade(ConfigInterface):
    def __init__(self, file: str, env: str = 'prod', root_directory: str = '.', transform_path_to_real: bool = True, enable_cache: bool = True):
        self._mapping_specials = {
            'root_path': realpath(root_directory)
        }

        self._file = root_directory + os.path.sep + file
        self._parser = ConfigParser()
        self._parser.read(self._file)
        self._env = env
        self._transform_path_to_real = transform_path_to_real
        self._cache_enabled = enable_cache
        self.cache = {}
        self._root_directory = root_directory

    def add_special(self, special_key: str, special_value: str):
        self._mapping_specials[special_key] = special_value

    def get(self, key: str, default=None):
        try:
            result = self._parser.get(self._env, key)

        except NoOptionError:
            return default

        value = ConfigParserFacade._auto_transform_type(result)

        if type(value) is str:
            return self._replace_specials(value)

        return value

    def set(self, key: str, value) -> ConfigInterface:
        self._parser.set(self._env, key, value)

        return self

    @staticmethod
    def _auto_transform_type(value):
        """
            Convert value get at string to type, with checking the value
            str => new type :
                True or true => bool(True)
                value => str("value")
                "value" => str("\"value\"")
                3.14 => float(3.14)
                15 => int(15)
        """
        if value.lower() == 'true':
            return True

        if value.lower() == 'false':
            return False

        # pas génial mais ça peut éviter les accesseurs fastidieux du parseur
        if value.isdecimal():
            try:
                return int(value)
            except ValueError:
                pass

        try:
            return float(value)
        except ValueError:
            pass

        return value

    def _replace_specials(self, value: str):
        return value.format_map(self._mapping_specials)
