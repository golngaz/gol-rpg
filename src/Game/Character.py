from pygame import Surface
from src.Game.Charset import Charset


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
        self._dx = 0.0
        self._dy = 0.0

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
        # todo avoir un speed max

        self._compute_speeds(tick)
        self._compute_position()
        self._compute_movement(tick)
        self._compute_screen_collision(limit)

        self._x += self._dx
        self._y += self._dy

    def _compute_speeds(self, tick: float):
        if self._move_up:
            self._dy = self._accelerate(tick, self._dy, -self._acceleration)

        if self._move_left:
            self._dx = self._accelerate(tick, self._dx, -self._acceleration)

        if self._move_right:
            self._dx = self._accelerate(tick, self._dx, self._acceleration)

        if self._move_down:
            self._dy = self._accelerate(tick, self._dy, self._acceleration)

        if not self._move_up and not self._move_down:
            self._dy = self._decelerate(tick, self._dy, self._deceleration)

        if not self._move_left and not self._move_right:
            self._dx = self._decelerate(tick, self._dx, self._deceleration)

    def _accelerate(self, tick: float, attribute: float, acceleration: float) -> float:
        """
        :param acceleration: can be negative
        :return:
        """

        # si l'acceleration est opposé à la vitesse, on freine d'abord
        if acceleration < 0 < attribute or acceleration > 0 > attribute:
            return self._decelerate(tick, attribute, self._deceleration)

        if attribute >= self._max_speed:
            return self._max_speed

        if attribute <= -self._max_speed:
            return -self._max_speed

        computed = tick * acceleration + attribute
        if computed > self._max_speed:
            return self._max_speed

        if computed < -self._max_speed:
            return -self._max_speed

        return computed

    def _decelerate(self, tick: float, attribute: float, deceleration: float) -> float:
        """
        :param deceleration: absolute value, will bring near 0
        """
        if deceleration < 0:
            raise Exception('Deceleration value can be lesser than 0')

        if attribute == 0:
            return 0

        negative = False
        if attribute < 0:
            negative = True
            attribute = -attribute

        if attribute - (tick * deceleration) < 0:
            return 0

        attribute = attribute - tick * deceleration

        if negative:
            return -attribute

        return attribute

    def _compute_position(self):
        """
        calcule l'affichage de la position du charset
        en fonction de la vitesse actuelle du personnage
        """

        if self._dx == 0 and self._dy == 0:
            return

        if abs(self._dx) > abs(self._dy):
            if self._dx > 0:
                self._charset.set_position(2)
            else:
                self._charset.set_position(1)
        else:
            if self._dy > 0:
                self._charset.set_position(0)
            else:
                self._charset.set_position(3)

    def _compute_movement(self, tick):
        # we advance movement only if the player has enough speed
        if abs(self._dx) + abs(self._dy) < self._max_speed / 2:
            self._charset.set_default_movement()
            return

        self._ticks_before_switch_movements += tick
        if self._ticks_before_switch_movements >= self._movements_all_x_seconds:
            self._charset.next_movement()
            self._ticks_before_switch_movements = 0

    def _compute_screen_collision(self, limit: Surface):
        self._x += self._dx
        self._y += self._dy

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
            round(self._dx, 2),
            round(self._dy, 2)
        )
