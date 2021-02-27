import os
from pygame import Rect
from src.Core import Core
from src.Editor import Editor
from src.Editor.TilesetDisplayer import TilesetDisplayer
from src.Game.MapDisplayer import MapDisplayer
from src.Game.Sprite import Sprite
from src.Menu.Button import Button


class ButtonOpenTileset(Button):
    def __init__(self, editor: Editor, x: float = 0, y: float = 0):
        self._editor = editor

        # @todo normaliser les path en finissant par des / pour éviter de l'ajouter à la main
        file = editor.config().get('tileset.menu.path') + os.path.sep + 'button-template.png'

        # @todo voir si on laisse ce paramètre et si on le monte dans un element
        self._x = x
        self._y = y
        super().__init__(Rect(self._x, self._y, 319, 72), file)

    def _init_sprites(self):
        if self._image is None:
            raise Exception('Image is not loaded')

        self._sprite_active = Sprite(self._image, Rect(self._rect.width, 0, self._rect.width, self._rect.height))
        self._sprite_inactive = Sprite(self._image, Rect(0, 0, self._rect.width, self._rect.height))

    def on_click(self, x: float, y: float, core: Core):
        core.displayer().get(TilesetDisplayer.name()).show()
        core.displayer().get(MapDisplayer.name()).pull_right()
