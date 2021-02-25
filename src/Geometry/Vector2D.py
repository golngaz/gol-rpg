from __future__ import annotations

import math
from math import cos, sin
from src.Geometry.Vector import Vector


class Vector2D(Vector):
    def __init__(self, x: float = 0.0, y: float = 0.0):
        super().__init__(x, y)
        self._x = x
        self._y = y

    def rotate(self, theta) -> Vector2D:
        new = super().rotate(theta)

        self.values = new.values
        self._x = self.values[0]
        self._y = self.values[1]

        return self

    def argument(self, radians=True):
        """
            Surcharge car on veut calculer par rapport à un angle trigonométrique
        """
        arg_in_rad = math.acos(Vector(1, 0) * self / self.norm())

        if self._y < 0:
            arg_in_rad = -arg_in_rad

        if radians:
            return arg_in_rad
        return math.degrees(arg_in_rad)

    def set_norm(self, norm: float):
        argument = self.argument(True)
        self.set_x(cos(argument) * norm)
        self.set_y(sin(argument) * norm)

    def x(self) -> float:
        return self._x

    def set_x(self, x: float) -> Vector2D:
        super().__init__(x, self._y)
        self._x = x

        return self

    def y(self) -> float:
        return self._y

    def set_y(self, y: float) -> Vector2D:
        super().__init__(self._x, y)
        self._y = y

        return self
