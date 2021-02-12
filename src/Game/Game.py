from src.AbstractEngine import AbstractEngine
from src.Config.ConfigInterface import ConfigInterface
from src.Game.Character import Character
from src.Game.Charset import Charset
from src.Game.MapDisplayer import MapDisplayer
from src.Game.MapFactory import MapFactory
from src.Listener.CharacterListener import CharacterListener
from src.Listener.DisplayListener import DisplayListener
from src.Listener.QuitListener import QuitListener


class Game(AbstractEngine):
    def __init__(self, config: ConfigInterface):
        super().__init__(config)
        self._player = Character(Charset(config.get('charset.path') + '/armored-npcs.png', 48, 72, 8, 3, 4, 4))

        self._init_dispatcher()
        self._core.configure_displayer(self)

    def run(self):
        self._core.run()

    def _init_dispatcher(self):
        self._dispatcher.add_listener(CharacterListener(self))
        self._dispatcher.add_listener(DisplayListener(self))
        self._dispatcher.add_listener(QuitListener(self))

    def configure_displayer(self, map_displayer: MapDisplayer, map_factory: MapFactory):
        map_displayer.add_map(map_factory.map('start-map'))
        map_displayer.set_current_map('start-map')
        map_displayer.add_characters(self._player)

    def player(self) -> Character:
        return self._player

    def quit(self) -> None:
        self._core.quit()
