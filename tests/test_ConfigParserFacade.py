import unittest
from src.Config.ConfigInterface import ConfigInterface
from src.Config.ConfigParserFacade import ConfigParserFacade
from tests.TestCase import TestCase


class ConfigParserFacadeTest(TestCase):
    def setUp(self):
        self._config = ConfigParserFacade('./asset/conf.ini', 'dev')

    def test_instance(self):
        self.assertIsInstance(self._config, ConfigInterface)

    def test_get(self):
        self.assertSame('bar', self._config.get('foo'))
        self.assertSame('dot', self._config.get('dot.dot'))

    def test_get_str_trap(self):
        self.assertSame('\'barman\'', self._config.get('foobar'))
        self.assertSame('\"barman\"', self._config.get('foobar_double'))

    def test_get_int(self):
        self.assertSame(24, self._config.get('figure'))

    def test_get_float(self):
        self.assertSame(3.14, self._config.get('float'))

    def test_get_bool(self):
        self.assertSame(True, self._config.get('my_bool'))
        self.assertSame(False, self._config.get('my_bool2'))

    def test_get_with_default(self):
        self.assertSame('bar', self._config.get('foo', 'patate'))
        self.assertSame('carotte', self._config.get('fooooooooooo', 'carotte'))

    def test_with_another_env(self):
        config = ConfigParserFacade('./asset/conf.ini', 'env2')
        self.assertSame('bar2', config.get('foo'))

    def test_set(self):
        self._config.set('machin', 'truc')
        self.assertSame('truc', self._config.get('machin'))

    def test_set_will_not_write_on_ini_file(self):
        self._config.set('machin', 'truc')
        config2 = ConfigParserFacade('./asset/conf.ini', 'dev')

        self.assertIsNone(config2.get('machin'))

    def test_path_transform(self):
        self.assertSame('E:\\gael\\dev\\gol-rpg\\tests/machin', self._config.get('my.path'))

        with self.assertRaises(KeyError) as e:
            self._config.get('special.path')

        self.assertSame('\'special_custom\'', str(e.exception))

        self._config.add_special('special_custom', 'custom_path')
        self.assertSame('my/custom_path/is/special', self._config.get('special.path'))


if __name__ == '__main__':
    unittest.main()
