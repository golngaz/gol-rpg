from pygame import Surface
from src.Game.Charset import Charset
from src.Geometry.Vector2D import Vector2D


class Character:
    """
        Entitée qui pourra se déplacer sur l'écran
        possédant un charset configurable
    """

    def __init__(self, charset: Charset):
        # movements
        self._move_down = False
        self._move_up = False
        self._move_left = False
        self._move_right = False
        self._movements_all_x_seconds = 0.2
        self._ticks_before_switch_movements = 0

        self._charset = charset
        self._x = 0.0
        self._y = 0.0

        # speeds
        self._max_speed = 3
        self._speed = Vector2D()

        # 10 acceleration at 10 px by tick
        self._acceleration = 10.0
        self._deceleration = 10.0

    def load(self):
        self._charset.load()

    def draw(self, surface: Surface):
        # todo à faire hériter d'une classe abstraite pour afficher un Objet dans le jeu

        self._charset.sprite().draw(surface, (self._x, self._y))

    def move_down(self):
        self._move_down = True

    def move_down_stop(self):
        self._move_down = False

    def move_up(self):
        self._move_up = True

    def move_up_stop(self):
        self._move_up = False

    def move_left(self):
        self._move_left = True

    def move_left_stop(self):
        self._move_left = False

    def move_right(self):
        self._move_right = True

    def move_right_stop(self):
        self._move_right = False

    def tick(self, tick: float, limit: Surface):
        self._compute_speeds(tick)
        self._compute_position()
        self._compute_movement(tick)

        self._apply_position()

        self._compute_screen_collision(limit)

    def _compute_speeds(self, tick: float):
        if self._move_up:
            self._accelerate(tick, 'y', self._acceleration)

        if self._move_left:
            self._accelerate(tick, 'x', -self._acceleration)

        if self._move_right:
            self._accelerate(tick, 'x', self._acceleration)

        if self._move_down:
            self._accelerate(tick, 'y', -self._acceleration)

        if not self._move_up and not self._move_down:
            self._decelerate(tick, 'y', self._deceleration)

        if not self._move_left and not self._move_right:
            self._decelerate(tick, 'x', self._deceleration)

        self._limit_speed()

    def _accelerate(self, tick: float, attribute: str, acceleration: float):
        """
        :param acceleration: can be negative
        :param attribute: x or y
        """

        if attribute == 'x':
            self._speed.set_x(tick * acceleration + self._speed.x())

        elif attribute == 'y':
            self._speed.set_y(tick * acceleration + self._speed.y())

    def _limit_speed(self):
        if self._speed.norm() > self._max_speed:
            self._speed.set_norm(self._max_speed)

    def _decelerate(self, tick: float, attribute: str, deceleration: float):
        """
        :param deceleration: absolute value, will bring near 0
        """

        if attribute == 'x':
            value = self._speed.x()
        else:
            value = self._speed.y()

        if deceleration < 0:
            raise Exception('Deceleration value can be lesser than 0')

        if value == 0:
            return

        negative = False
        if value < 0:
            negative = True
            value = -value

        value = value - tick * deceleration

        if value < 0:
            value = 0

        if negative:
            value = -value

        if attribute == 'x':
            self._speed.set_x(value)
        else:
            self._speed.set_y(value)

    def _compute_position(self):
        """
        calcule l'affichage de la position du charset
        en fonction de la vitesse actuelle du personnage
        """

        # todo test small values
        if self._speed.norm() == 0:
            return

        if abs(self._speed.x()) > abs(self._speed.y()):
            if self._speed.x() > 0:
                self._charset.set_position(2)
            else:
                self._charset.set_position(1)
        else:
            if self._speed.y() > 0:
                self._charset.set_position(3)
            else:
                self._charset.set_position(0)

    def _compute_movement(self, tick):
        # we advance movement only if the player has enough speed
        if abs(self._speed.x()) + abs(self._speed.y()) < self._max_speed / 2:
            self._charset.set_default_movement()
            return

        self._ticks_before_switch_movements += tick
        if self._ticks_before_switch_movements >= self._movements_all_x_seconds:
            self._charset.next_movement()
            self._ticks_before_switch_movements = 0

    def _compute_screen_collision(self, limit: Surface):
        offset_x = limit.get_offset()[0]
        offset_y = limit.get_offset()[1]

        if self._x + self._charset.width > limit.get_width() + offset_x:
            self._x = offset_x + limit.get_width() - self._charset.width
        elif self._x < offset_x:
            self._x = offset_x

        if self._y + self._charset.height > limit.get_height() + offset_y:
            self._y = offset_y + limit.get_height() - self._charset.height
        elif self._y < offset_y:
            self._y = offset_y

    def __str__(self):
        return 'x: {}, y: {}, dx: {}, dy: {}'.format(
            round(self._x, 2),
            round(self._y, 2),
            round(self._speed.x(), 2),
            round(self._speed.y(), 2)
        )

    def _apply_position(self):
        self._x += self._speed.x()
        self._y -= self._speed.y()
