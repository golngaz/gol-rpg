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

        self._map_factory = MapFactory(config)
        self._map_displayer = MapDisplayer(config)

        self._init_dispatcher()
        self.configure_displayer()

    def run(self):
        self._core.run()

    def _init_dispatcher(self):
        self._dispatcher.add_listener(CharacterListener(self))
        self._dispatcher.add_listener(DisplayListener(self))
        self._dispatcher.add_listener(QuitListener(self))

    def configure_displayer(self):
        self._map_displayer.add_map(self._map_factory.map('start-map'))
        self._map_displayer.set_current_map('start-map')
        self._map_displayer.add_characters(self._player)
        self._core.displayer().add_displayer(self._map_displayer)

    def player(self) -> Character:
        return self._player

    def quit(self) -> None:
        self._core.quit()
