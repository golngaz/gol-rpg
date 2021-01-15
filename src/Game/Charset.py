from ctypes import Union

import pygame
from pygame.surface import Surface


class Charset:
    def __init__(
            self,
            file: str,
            width: float,
            height: float,
            skins: int = 1,
            movements: int = 3,
            positions: int = 4,
            skin: int = 1
    ):
        """
        :param file: fichier correspondant au charset
        :param skins: nb skins
        :param movements: nb movements
        :param positions: nb positions
        """

        self._image = None
        self._file = file
        self._width = width
        self._height = height

        if skins == 0 or movements == 0 or positions == 0:
            raise Exception('Error arguments')

        self._skins = skins
        self._movements = movements
        # 1 for increase, 0 for decrease
        self._movement_way = 1
        self._positions = positions

        self._skin = skin
        self._movement = 0
        self._position = 0

    def set_skin(self, skin):
        """
        :param skin: 0 to nb skins => bottom, left, right, top
        """
        if skin > self._skins:
            raise Exception('{} is out of skins total {}'.format(skin, self._skins))
        self._skin = skin

        return self

    def set_movement(self, movement):
        """
        :param movement: 0 to nb movements
        """
        if movement > self._movements:
            raise Exception('{} is out of movements total {}'.format(movement, self._movements))

        self._movement = movement

        return self

    def set_position(self, position):
        """
        :param position: 0 to nb positions
        """
        if position > self._positions:
            raise Exception('{} is out of positions total {}'.format(position, self._positions))

        self._position = position

        return self

    def load(self) -> None:
        self._image = pygame.image.load(self._file).convert_alpha()

    def image(self) -> Surface:
        if not self._image:
            raise Exception('image is not loaded')

        # todo mettre en param le movement et position
        return self._image

    def rect(self):
        # 4 is modulo of nb skin before go back to another line
        return pygame.Rect(
            self._movement * self._width +
            (self._skin % 4) * self._width * self._movements,
            self._position * self._height +
            int((self._skin - (self._skin % 4)) / 4) * self._height * self._positions,
            self._width,
            self._height
        )

    def next_movement(self):
        # todo warning, manage only 3 movements with neutral at 1
        if self._movement + self._movement_way >= self._movements or self._movement + self._movement_way < 0:
            self._movement_way = -self._movement_way
            self._movement += self._movement_way
            return

        self._movement += self._movement_way

    def set_default_movement(self):
        self._movement = 1
        self._movement_way = 1
