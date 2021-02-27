import os
from src.AbstractEngine import AbstractEngine
from src.Config.ConfigInterface import ConfigInterface
from src.Editor.Action.ButtonOpenTileset import ButtonOpenTileset
from src.Editor.EditorDisplayer import EditorDisplayer
from src.Editor.TilesetDisplayer import TilesetDisplayer
from src.Game.Character import Character
from src.Game.MapDisplayer import MapDisplayer
from src.Game.MapFactory import MapFactory
from src.Listener.DisplayListener import DisplayListener
from src.Listener.Menu.ClickElementListener import ClickElementListener
from src.Listener.QuitListener import QuitListener


class Editor(AbstractEngine):
    def __init__(self, config: ConfigInterface):
        super().__init__(config)

        self._displayer.set_background(True, (10, 200, 5))
        self._map_factory = MapFactory(config)
        self._map_displayer = MapDisplayer(config)
        self._editor_displayer = EditorDisplayer()

        file = config.get('tileset.default.path') + os.path.sep + 'Tileset_48x48_1.png'
        self._tileset_displayer = TilesetDisplayer(file)
        
        self._configure_map_displayer()
        self._configure_editor_displayer()
        self._configure_tileset_displayer()

        self._init_dispatcher()

    def run(self):
        self._core.load()
        self._core.run()

    def _configure_map_displayer(self):
        self._map_displayer.add_map(self._map_factory.map('start-map'))
        self._map_displayer.set_current_map('start-map')
        self._displayer.add_displayer(self._map_displayer)

    def _init_dispatcher(self):
        self._dispatcher.add_listener(QuitListener(self))
        self._dispatcher.add_listener(DisplayListener(self))
        # todo passer par une factory/ un provider pour les éléments et le listener ?
        self._dispatcher.add_listener(ClickElementListener(self, self._editor_displayer.elements()))

    def _configure_editor_displayer(self):
        self._editor_displayer.add_element(ButtonOpenTileset(self, 10, 10))
        self._displayer.add_displayer(self._editor_displayer)

    def player(self) -> Character:
        pass

    def quit(self):
        self._core.quit()

    def _configure_tileset_displayer(self):
        self._tileset_displayer.hide()
        self._tileset_displayer.set_pos(0, 300)
        self._displayer.add_displayer(self._tileset_displayer)
