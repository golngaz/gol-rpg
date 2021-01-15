from src.Config.Config import Config
from tests.TestCase import TestCase


class ConfigTest(TestCase):
    def test_default_value(self):
        config = Config()
        self.assertEqual({}, config._data)

    def test_init(self):
        config = Config({'foo': 'bar'})

        self.assertEqual({'foo': 'bar'}, config._data)

    def test_get(self):
        config = Config({'foo': 'bar'})

        self.assertEqual('bar', config.get('foo'))
        self.assertEqual(None, config.get('bar'))
        self.assertEqual(3.14, config.get('bar', 3.14))

    def test_set(self):
        config = Config()

        config.set('foo', 'bar')
        self.assertEqual({'foo': 'bar'}, config._data)
        self.assertEqual('bar', config.get('foo'))


if __name__ == '__main__':
    unittest.main()
