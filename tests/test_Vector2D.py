import math
import unittest
from src.Config.ConfigParserFacade import ConfigParserFacade
from src.Geometry.Vector2D import Vector2D
from tests.TestCase import TestCase


class Vector2DTest(TestCase):
    def setUp(self):
        self._config = ConfigParserFacade('./asset/conf.ini', 'dev')

    def test_argument_x_positive_y_positive(self):
        a = Vector2D(4, 4)

        self.assertAlmostEqual(math.pi / 4, a.argument())

    def test_argument_x_negative_y_positive(self):
        a = Vector2D(-4, 4)

        self.assertAlmostEqual(3 * math.pi / 4, a.argument())

    def test_argument_x_negative_y_negative(self):
        a = Vector2D(-4, -4)

        self.assertAlmostEqual(- 3 * math.pi / 4, a.argument())

    def test_argument_x_positive_y_negative(self):
        a = Vector2D(4, -4)

        self.assertAlmostEqual(- math.pi / 4, a.argument())

    def test_norm(self):
        a = Vector2D(0.7, 1)

        self.assertAlmostEqual(1.2207, a.norm(), places=4)

    def test_set_norm(self):
        a = Vector2D(0.7, 1)

        a.set_norm(1)
        self.assertAlmostEqual(1, a.norm(), places=1)
        self.assertAlmostEqual(0.57346, a.x(), places=5)
        self.assertAlmostEqual(0.81923, a.y(), places=5)

    def test_set_norm_0(self):
        a = Vector2D(6, 0)

        a.set_norm(2)
        self.assertAlmostEqual(2, a.x())
        self.assertAlmostEqual(0, a.y())

    def test_set_norm_90(self):
        a = Vector2D(0, 2)

        a.set_norm(1)
        self.assertAlmostEqual(0, a.x())
        self.assertAlmostEqual(1, a.y())

    def test_set_norm_180(self):
        a = Vector2D(-4, 0)

        a.set_norm(1)
        self.assertAlmostEqual(-1, a.x())
        self.assertAlmostEqual(0, a.y())

    def test_set_norm_270(self):
        a = Vector2D(0, -5)

        a.set_norm(3)
        self.assertAlmostEqual(0, a.x())
        self.assertAlmostEqual(-3, a.y())

    def test_set_norm_315(self):
        a = Vector2D(5, 0)
        a.rotate(315)
        a.set_norm(2)

        self.assertAlmostEqual(math.sqrt(2), a.x())
        self.assertAlmostEqual(-math.sqrt(2), a.y())

    def test_rotate_norm_to_2(self):
        a = Vector2D(2, 0)
        a.rotate(315)

        self.assertAlmostEqual(- math.pi / 4,  a.argument())
        self.assertAlmostEqual(math.sqrt(2), a.x())
        self.assertAlmostEqual(- math.sqrt(2), a.y())

    def test_rotate_simple(self):
        a = Vector2D(1, 0)
        a.rotate(315)

        self.assertAlmostEqual(- math.pi / 4,  a.argument())
        self.assertAlmostEqual(math.sqrt(2) / 2, a.x())
        self.assertAlmostEqual(- math.sqrt(2) / 2, a.y())

    def test_rotate(self):
        a = Vector2D(5, 0)
        a.rotate(315)

        self.assertAlmostEqual(- math.pi / 4,  a.argument())
        self.assertAlmostEqual(3.535533, a.x(), places=5)
        self.assertAlmostEqual(-3.535533, a.y(), places=5)


if __name__ == '__main__':
    unittest.main()
