import os
from pygame import Rect
from src.Core import Core
from src.Editor.EditorDisplayer import EditorDisplayer
from src.Game.Sprite import Sprite
from src.Menu.Button import Button


class ButtonOpenTileset(Button):
    def __init__(self, config, x: float = 0, y: float = 0):
        # @todo normaliser les path en finissant par des / pour éviter de l'ajouter à la main
        file = config.get('tileset.menu.path') + os.path.sep + 'button-tileset-200-50.png'

        # @todo supprimer
        self._config = config

        # @todo voir si on laisse ce paramètre et si on le monte dans un element
        self._x = x
        self._y = y
        super().__init__(Rect(self._x, self._y, 200, 50), file)

    def _init_sprites(self):
        if self._image is None:
            raise Exception('Image is not loaded')

        self._sprite_active = Sprite(self._image, Rect(200, 0, 200, 50))
        self._sprite_inactive = Sprite(self._image, Rect(0, 0, 200, 50))

    def on_click(self, x: float, y: float, core: Core):
        button = ButtonOpenTileset(self._config, 100, self._y + 50)
        button.load()

        core.displayer().get(EditorDisplayer.name()).add_element(button)
