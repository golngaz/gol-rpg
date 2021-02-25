import unittest


class TestCase(unittest.TestCase):
    def assertSame(self, expected, actual, message: str = ''):
        self.assertEqual(type(expected), type(actual), message)
        self.assertEqual(expected, actual, message)
