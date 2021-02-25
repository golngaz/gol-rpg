from pygame.rect import Rect
from pygame.surface import Surface


class Sprite:
    def __init__(self, image: Surface, rect: Rect):
        self._image = image
        self._rect = rect

    def draw(self, surface: Surface, coords: tuple):
        surface.blit(self._image, coords, self._rect)
