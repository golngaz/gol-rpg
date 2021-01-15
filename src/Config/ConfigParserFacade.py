from __future__ import annotations
from configparser import ConfigParser, NoOptionError
from src.Config.ConfigInterface import ConfigInterface


class ConfigParserFacade(ConfigInterface):
    def __init__(self, file: str, env: str = 'prod'):
        self._file = file
        self._parser = ConfigParser()
        self._parser.read(file)
        self._env = env

    def get(self, key: str, default=None):
        try:
            result = self._parser.get(self._env, key)

        except NoOptionError:
            return default

        return ConfigParserFacade._auto_transform_type(result)

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
